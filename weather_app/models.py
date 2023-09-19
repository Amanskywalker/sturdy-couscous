from django.db import models
from django.contrib.auth.models import User

class SearchData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=100) # city name
    city_id = models.CharField(max_length=100) # city unique ID
    weather = models.TextField() # just to store the weather information recived form the API
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city