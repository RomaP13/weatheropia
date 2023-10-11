# Weatheropia

This is a simple weather application that allows users to search for cities, view the current weather, and check the weather forecast. The application supports two languages: English and Ukrainian. It provides weather information only for Ukrainian cities.

![app-preview](preview.png)

## Installation
1. Clone this repository:
```
   git clone https://github.com/RomaP13/weatheropia.git
   cd weatheropia
```
2. Install the required Python packages:
```
pip install -r requirements.txt
```
3. Run the migrations to create the database:
```
python manage.py migrate
```
4. Start the development server:
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
