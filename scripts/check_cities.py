# This file checks if there is weather information
# for cities in openweatherapi

import requests
from termcolor import cprint
from weatherapp.models import City


# Function to check weather information using the OpenWeatherAPI
def check_weather(url, city):
    print(f"INFO: CHECK {city}")
    response = requests.get(url).json()

    # If the city is not found in the API response
    if not response:
        cprint(f"+++ERROR: {city} IS NOT FOUND+++", "red")
        return True
    else:
        cprint(f"INFO: {city} IS FOUND", "green")
        return False


def run():
    cities = City.objects.all().order_by("id")

    api_key = open("API_KEY").read()
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    # Check the weather for each city
    counter = 0
    for city in cities:
        url = base_url + "appid=" + api_key + "&q=" + city.name_en
        if(check_weather(url, city.name_en)):
            counter += 1

    print(f"RESULT: {counter} CITIES IS NOT FOUND")
