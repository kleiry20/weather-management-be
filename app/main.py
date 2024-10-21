from fastapi import FastAPI
from dotenv import load_dotenv
from app.middleware.cors import setup_cors
from app.api.routes import router

load_dotenv() 

app = FastAPI()

# Set up CORS
setup_cors(app)

# Include API routes
app.include_router(router)
