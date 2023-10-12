import requests
from datetime import datetime


def get_current_weather(city, lang):
    api_key = open("API_KEY").read().replace("\n", "")
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    url = base_url + "appid=" + api_key + "&q=" + city + "&lang=" + lang
    response = requests.get(url).json()

    current_weather = {
        "temp_celsius": int(response["main"]["temp"] - 273.15),
        "humidity": response["main"]["humidity"],
        "sunrise_time": datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"]),
        "sunset_time": datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"]),
        "wind_speed": response["wind"]["speed"],
        "description": response["weather"][0]["description"].capitalize(),
    }

    return current_weather


def get_weekly_forecast(city, lang):
    api_key = open("API_KEY").read().replace("\n", "")
    base_url = "https://api.openweathermap.org/data/2.5/forecast?"

    url = base_url + "appid=" + api_key + "&q=" + city + "&lang=" + lang
    response = requests.get(url).json()

    forecast_list = response["list"]
    weekly_forecast = []
    for forecast in forecast_list:
        timestamp = forecast["dt"]
        date = datetime.utcfromtimestamp(timestamp)
        current_day = datetime.now().day
        day = date.day
        hour = date.hour

        if hour == 15 and day != current_day:
            weekly_forecast.append({
                "date": date,
                "temp_celsius": int(forecast["main"]["temp"] - 273.15),
                "humidity": forecast["main"]["humidity"],
                "wind_speed": forecast["wind"]["speed"],
                "description": forecast["weather"][0]["description"].capitalize(),
            })

    return weekly_forecast
