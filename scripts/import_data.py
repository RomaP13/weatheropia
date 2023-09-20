# This file reads data from a CSV file and populates a database table
# with cities' names

import csv
from weatherapp.models import City


def run():
    with open("scripts/data/cities.csv") as file:
        reader = csv.reader(file)

        City.objects.all().delete()

        for row in reader:
            city = City(name_en=row[0], name_uk=row[1])
            city.save()
            print(f"INFO: add {city}")
