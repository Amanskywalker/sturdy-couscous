# Sturdy Couscous

## Description

The Sturdy Couscous is a web application that allows users to search for weather information for different cities. It integrates with a third-party weather API to fetch weather data and displays it to the users in a user-friendly manner, currently it limited to next 12 hours forcast only.

The app provides the following main features:

- **User Registration and Authentication:** Users can sign up and log in to the app to access its features.

- **City Search:** Users can search for weather information by entering the name of a city.

- **Weather Cards:** The app displays weather information for the searched city in the form of Bootstrap cards. Each card provides details such as date and time, weather, temperature, and precipitation probability.

## Technologies Used

- Python
- Django and Django Restframework
- Bootstrap
- JavaScript

## Installation

1. Clone the repository to your local machine:
    ```
    git clone https://github.com/Amanskywalker/sturdy-couscous.git
    ```
2. Navigate to the project directory:
    ```
    cd sturdy-couscous
    ```
3. Initalize pipenv environment:
    ```
    pipenv --python 3.11
    ```
4. Install the project dependencies:
    ```
    pipenv install 
    ```
5. Apply migrations:
    ```
    python manage.py migrate
    ```
6. Start the development server:
    ```
    python manage.py runserver
    ```

## Usage

1. Register or log in to the app (optional).

2. Enter the name of a city in the search bar and click the "Get Weather" button.

3. View the weather information for the searched city.

## License

This project is licensed under the MIT License

## Acknowledgements
following are the tech used in this project

- [Django](djangoproject.com)
- [Django Restframework](www.django-rest-framework.org)
- [Bootstrap](getbootstrap.com)
- [AccuWeather API](developer.accuweather.com)