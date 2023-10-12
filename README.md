# Weatheropia

This is a simple weather application that allows users to search for cities, view the current weather, and check the weather forecast. The application supports two languages: English and Ukrainian. It provides weather information only for Ukrainian cities.

![app-preview](preview.png)

## API KEY
In order to use this program, you will need to obtain an API key by signing up with [this site](https://openweathermap.org/api).

## Installation
1. Clone this repository:
```
   git clone https://github.com/RomaP13/weatheropia.git
   cd weatheropia
```

2. Create a file named "API_KEY" and add your key in this file.

3. Install the required Python packages:
```
pip install -r requirements.txt
```

4. Run the migrations to create the database:
```
python manage.py migrate --run-syncdb
```

5. Run the following scripts:
```
python scripts/main.py
python manage.py runscript import_data
```

6. Start the development server:
```
python manage.py runserver
```

## Usage
1. Enter the name of a Ukrainian city in the search bar.
2. Select the desired city from the search results.
3. View the current weather and weather forecast for the selected city.
4. You can switch between English and Ukrainian languages using the language dropdown in the navigation menu.

## License
[MIT](https://choosealicense.com/licenses/mit/)
