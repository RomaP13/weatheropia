from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import City
from .weatherapi import get_current_weather, get_weekly_forecast


def index(request):
    columns = range(1, 3)
    cities = City.objects.all().order_by("id")
    per_page = 10
    paginator = Paginator(cities, per_page)
    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)
    page = paginator.get_page(page_number)

    cities_0_to_4 = page_obj[:5]
    cities_5_to_9 = page_obj[5:]

    context = {
        "columns": columns,
        "cities1": cities_0_to_4,
        "cities2": cities_5_to_9,
        "page": page,
        "error_message": "",
    }

    city_name = request.GET.get("city")
    if city_name:
        try:
            city = City.objects.get(name_en=city_name)
            return redirect('city', city=city_name)
        except City.DoesNotExist:
            error_message = f"City '{city_name}' not found in the database."
            context["error_message"] = error_message

    return render(request, "index.html", context)


def city(request, city):
    current_weather = get_current_weather(city)
    weekly_forecast = get_weekly_forecast(city)
    context = {
        "weather": current_weather,
        "forecast": weekly_forecast,
        "city": city,
    }

    return render(request, "city.html", context)
