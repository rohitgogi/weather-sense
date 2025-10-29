import requests


URL = "https://geocoding-api.open-meteo.com/v1/search?name="
WEATHER_URL = "https://api.open-meteo.com/v1/forecast?" # ex https://api.open-meteo.com/v1/forecast?latitude=42.98339&longitude=-81.23304&hourly=temperature_2m
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    80: "Rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
}


def get_coordinates(city: str):
    response = requests.get(URL + city).json()
    latitude = response.get("results")[1].get("latitude")
    longitude = response.get("results")[1].get("longitude")
    return latitude, longitude

def get_weather(city: str):
    coordinates = get_coordinates(city)
    modified_url = WEATHER_URL + "latitude=" + str(coordinates[0]) + "&longitude=" + str(coordinates[1]) + "&current_weather=true"
    response = requests.get(modified_url).json()
    response["city"] = city
    response = response_cleanup(response)
    return response

def response_cleanup(response: str):
    del response["generationtime_ms"]
    del response["utc_offset_seconds"]
    del response["timezone"]
    del response["timezone_abbreviation"]
    del response["elevation"]
    del response["current_weather_units"]
    response["temperature"] = response.get("current_weather").get("temperature")
    response["windspeed"] = response.get("current_weather").get("windspeed")
    response["time"] = response.get("current_weather").get("time")
    response["description"] = WEATHER_CODES.get(response.get("current_weather").get("weathercode"))
    del response["current_weather"]
    return response
    
print(get_weather("London"))