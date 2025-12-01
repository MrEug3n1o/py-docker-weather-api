import requests
import os

from dotenv import load_dotenv
load_dotenv()


def get_weather() -> None:
    weather = {
        "q": "Paris",
        "key": os.getenv("API")
    }
    url = "http://api.weatherapi.com/v1/current.json"
    response = requests.get(url, params=weather)
    print(response.json())


if __name__ == "__main__":
    get_weather()
