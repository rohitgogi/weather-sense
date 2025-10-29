from fastapi import FastAPI
from app.weather import get_weather
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/weather")
def weather_endpoint(city: str):
    return get_weather(city)