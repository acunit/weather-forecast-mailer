import requests
import config

def get_weather_forecast():
    # Assigning the weather API link to the url variable
    # NOTE should hide API key before pushing to GitHub
    # Connecting to the weather api
    url = "http://api.openweathermap.org/data/2.5/weather?q=san+diego%2Cca&units=imperial&APPID=" + openweathermap_app_id
    # assign the JSON object returned from the get() to variable
    weather_request = requests.get(url)
    # convert the JSON to a dictionary
    weather_json = weather_request.json()

    # Parsing JSON
    # getting the description, temp_min, and temp_max from the api call
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # Creating our forecast string
    # assign the values to a string in order to send in the email.
    forecast = 'The San Diego forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return forecast