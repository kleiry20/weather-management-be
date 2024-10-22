import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

# To store data in a dictionary
weather_data_store = {}

cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

async def fetch_weather_data():
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            kelvin_temp = data['main']['temp']
            celsius_temp = kelvin_temp - 273.15
            feels_like_kelvin = data['main']['feels_like']
            feels_like_celsius = feels_like_kelvin - 273.15

            # Convert the 'dt' UNIX timestamp to a human-readable date and time
            # Extract timestamp and convert to date and time
            timestamp = data.get('dt')
            date_time = datetime.fromtimestamp(timestamp)
            date = date_time.strftime('%Y-%m-%d')
            time = date_time.strftime('%H:%M:%S')


            # Store the data in the dictionary
            weather_data_store[city] = {
                "temperature_celsius": round(celsius_temp, 2),
                "feels_like_celsius": round(feels_like_celsius, 2),
                "weather": data.get('weather', [{}])[0].get('description', 'N/A'),
                "main": data.get('main', {}),
                 "date": date,
                "time": time,
                "icon": data.get('weather', [{}])[0].get('icon')
            }
        else:
            print(f"Error fetching data for {city}: {response.json()}")
