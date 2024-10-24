from fastapi import FastAPI, WebSocket
from dotenv import load_dotenv
from app.middleware.cors import setup_cors
from app.api.routes import router
from app.api.scheduler import start_weather_scheduler  # Import the scheduler start function
from app.broadcast import add_client, remove_client, broadcast_weather_data  # Import your broadcast functions
from app.api.weather_fetcher import weather_data_store


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

# WebSocket endpoint for real-time updates
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await add_client(websocket)  # Add the new client
#     try:
#         while True:
#             await websocket.receive_text()  # Keep the connection alive
#     except:
#         await remove_client(websocket)  # Remove client on disconnect

# # Function to fetch weather data and broadcast it
# async def fetch_weather_data():
#     # Your logic to fetch weather data
#     new_weather_data = weather_data_store  # Replace with your actual fetched data
#     await broadcast_weather_data(new_weather_data)


active_connections = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await add_client(websocket)
    active_connections.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()  # Keep the connection alive
            await websocket.send_text(f"Message received: {data}")
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await remove_client(websocket)
        active_connections.remove(websocket)