# weather_fetcher.py
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
import json
import time

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
weather_data_store = {city: [] for city in cities}

def save_weather_data_to_file():
    with open('weather_data.json', 'w') as f:
        json.dump(weather_data_store, f, indent=4)

def fetch_all_weather_data():
    print("Scheduler is fetching weather data...")

    # Loop through each city and fetch data sequentially
    for city in cities:
        fetch_weather_data(city)
        time.sleep(10)  # Adds a small delay between each API call to avoid rate limits

    save_weather_data_to_file()
    print("Fetched data for all cities and saved.")

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        kelvin_temp = data['main']['temp']
        celsius_temp = kelvin_temp - 273.15
        feels_like_kelvin = data['main']['feels_like']
        feels_like_celsius = feels_like_kelvin - 273.15
        timestamp = data.get('dt')
        date_time = datetime.fromtimestamp(timestamp)
        date = date_time.strftime('%Y-%m-%d')
        time_str = date_time.strftime('%H:%M:%S')

        city_data = {
            "date": date,
            "time": time_str,
            "temperature_celsius": round(celsius_temp, 2),
            "feels_like_celsius": round(feels_like_celsius, 2),
            "weather": data.get('weather', [{}])[0].get('description', 'N/A'),
            "icon": data.get('weather', [{}])[0].get('icon', 'N/A')
        }

        weather_data_store[city].append(city_data)

        # Keep only the last 5 entries for each city to limit memory usage
        if len(weather_data_store[city]) > 5:
            weather_data_store[city].pop(0)

        print(f"Fetched and stored data for {city}: {city_data}")
    else:
        print(f"Error fetching data for {city}: {response.json()}")


def calculate_aggregates():
    aggregates = {}

    for city, data_points in weather_data_store.items():
        if data_points:
            total_temp = sum(entry["temperature_celsius"] for entry in data_points)
            average_temp = total_temp / len(data_points)
            latest_entry = data_points[-1]  # Get the most recent entry
            aggregates[city] = {
                "average_temperature": round(average_temp, 2),
                "latest_temperature": latest_entry["temperature_celsius"],
                "weather": latest_entry["weather"],
                # "timestamp": latest_entry.get("timestamp", "N/A")  # Added a default value
            }
    
    return aggregates