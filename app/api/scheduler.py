from apscheduler.schedulers.background import BackgroundScheduler
from app.api.weather_fetcher import fetch_all_weather_data

# Create a scheduler instance
scheduler = BackgroundScheduler()

# Schedule the `fetch_all_weather_data` function every 2 minutes
scheduler.add_job(fetch_all_weather_data, 'interval', minutes=2)

def start_weather_scheduler():
    print("Starting the background weather scheduler...")

    # Manually trigger the first fetch immediately
    fetch_all_weather_data()

    # Start the scheduler for subsequent intervals
    scheduler.start()
