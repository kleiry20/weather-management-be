# This file is to define API endpoints

from fastapi import APIRouter
from app.api.weather_fetcher import fetch_weather_data, weather_data_store, calculate_aggregates

router = APIRouter()

# @router.get("/weather/{city}")
# def weather_route(city: str):
#     return get_weather(city)

@router.get("/")
def read_root():
    return {"message": "Welcome to the Weather Monitoring API"}

# to fetch the weather data from openweather for all cities
# @router.get("/fetch_weather")
# async def get_weather():
#     await fetch_weather_data()  # Call the function to fetch and store weather data
#     return {"message": "Weather data fetched for all cities."}


# to get the fetched api data from openweather (temp storage) and pass to FE
@router.get("/weather_data")
def get_stored_weather_data():
    return {"weather_data": weather_data_store}

@router.get("/weather_aggregates")
def get_weather_aggregates():
    aggregates = calculate_aggregates()
    return {"aggregates": aggregates}
