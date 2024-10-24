# broadcast.py
from fastapi import WebSocket
from app.api.weather_fetcher import weather_data_store

clients = []

async def add_client(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

async def remove_client(websocket: WebSocket):
    if websocket in clients:
        clients.remove(websocket)

async def broadcast_weather_data():
    new_data = weather_data_store  # Get the latest data
    print(f"Broadcasting new data: {new_data}")

    # Send the latest data to all connected clients
    for client in clients:
        try:
            await client.send_json(new_data)
        except Exception as e:
            print(f"Error sending data to client: {e}")
