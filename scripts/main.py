# The file to get cities and write them in csv file

import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
    }

    req = requests.get(url, headers=headers)
    src = req.text

    with open("scripts/data/cities.html", "w") as file:
        file.write(src)


def load_data():
    # Read HTML source from the Ukrainian cities page
    with open("scripts/data/cities.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    tr_tags = soup.find(class_="wikitable").find("tbody").find_all("tr")

    cities_uk, cities_en = [], []
    for tag in tr_tags:
        td_tags = tag.find_all("td")

        if td_tags:
            city_en = td_tags[0].find("a").text
            city_uk = td_tags[1].find("a").text

            cities_en.append(city_en)
            cities_uk.append(city_uk)

    # Write extracted data to a CSV file
    for city_en, city_uk in zip(cities_en, cities_uk):
        with open("scripts/data/cities.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    city_en,
                    city_uk
                )
            )


def main():
    get_html("https://simple.wikipedia.org/wiki/List_of_cities_in_Ukraine")
    load_data()


if __name__ == "__main__":
    main()
