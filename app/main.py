import requests
import os


def get_weather() -> None:
    CITY = "Paris"
    weather = {
        "q": CITY,
        "key": os.getenv("API")
    }
    WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
    response = requests.get(WEATHER_API_URL, params=weather)
    print(response.json())


if __name__ == "__main__":
    get_weather()
