# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv() 
# api_key = os.getenv("OPENWEATHER_API_KEY")

# # List of cities
# cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']


# def get_weather(city: str):
#     if not api_key:
#         return {"error": "API key not found. Please set it in the .env file."}

#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         kelvin_temp = data['main']['temp']
#         celsius_temp = kelvin_temp - 273.15
#         return {"city": city, "temperature_celsius": round(celsius_temp, 2)}
#     else:
#         return {"error": "City not found or API call failed"}
