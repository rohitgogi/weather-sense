from smolagents import tool
from weather import get_weather


@tool
def current_weather(city: str) -> dict:
    """Given the city name, returns the JSON of the current weather of the city.

    Args:
        city: The name of the city to get weather for.
    """
    return get_weather(city)

@tool
def c_to_f(celsius: float) -> float:
    """Given the temperature in celsius, returns the temperature in fahrenheit
    
    Args:
        celsius: The temperature in celsius
    """
    return float((celsius * 9/5) + 32)

@tool
def compare_temps(city_a: str, city_b: str) -> dict:
    """Compare current temperatures between two cities.

    Args:
        city_a: First city name.
        city_b: Second city name.
    """
    a = get_weather(city_a)
    b = get_weather(city_b)
    warmer = city_a if a["temperature"] >= b["temperature"] else city_b
    return {"city_a": a, "city_b": b, "warmer_city": warmer}
