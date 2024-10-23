from fastapi import FastAPI
from dotenv import load_dotenv
from app.middleware.cors import setup_cors
from app.api.routes import router
from app.api.scheduler import start_weather_scheduler  # Import the scheduler start function

load_dotenv()

app = FastAPI()

# Set up CORS
setup_cors(app)

# Include API routes
app.include_router(router)

# Start the weather scheduler when the app starts
@app.on_event("startup")
def startup_event():
    start_weather_scheduler()  # Start the background scheduler
