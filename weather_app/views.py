from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
import requests
from .models import SearchData
from django.conf import settings
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

class AnonMinThrottle(AnonRateThrottle):
    scope = 'anon_min'

class AnonDayThrottle(AnonRateThrottle):
    scope = 'anon_day'

class HomePage(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

class AutocompleteCity(APIView):
    throttle_classes = [ AnonMinThrottle, AnonDayThrottle ]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    base_url = 'http://dataservice.accuweather.com'
    url = f'{base_url}/locations/v1/cities/autocomplete'

    @method_decorator(cache_page(60*60*2))
    def get(self, request):
        payload = {
            'apikey' : settings.WEATHER_API_KEY,
            'q' : request.GET.get("q"),
        }
        print(payload)
        res = requests.get(self.url, params=payload)
        print(res, res.json())
        if res.json() is None:
            return Response([], status=200)

        cities_list = res.json()
        cities = []
        for city in cities_list:
            cities.append({
                'name' : f"{city['LocalizedName']} ({city['Country']['LocalizedName']})",
                'key' : city["Key"]
            })
        return Response(cities, status=200)

class SerchCityWeather(APIView):
    throttle_classes = [ AnonMinThrottle, AnonDayThrottle ]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    base_url = 'http://dataservice.accuweather.com'
    url = f'{base_url}/forecasts/v1/hourly/12hour/'

    @method_decorator(cache_page(60*60*2))
    def get(self, request):
        city_id = request.GET.get("city_key")
        city_name = request.GET.get("city_name")

        payload = {
            'apikey' : settings.WEATHER_API_KEY,
        }
        print(payload)
        res = requests.get(f"{self.url}{city_id}", params=payload)
        
        print(res, res.json())
        store_data = SearchData.objects.create(
            user = request.user if request.user.is_authenticated else None,
            city = city_name,
            city_id = city_id,
            weather = res.json(),
        )

        return Response(res.json(), status=200)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})