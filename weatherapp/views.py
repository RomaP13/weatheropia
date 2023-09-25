from django.shortcuts import render
from django.core.paginator import Paginator
from .models import City


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
    }

    return render(request, "index.html", context)
