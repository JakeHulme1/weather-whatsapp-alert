import requests

# Function to get weather data from OpenWeatherMap API
def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Extract the weather description
    rain_chance = data['weather'][0]['description']
    return rain_chance