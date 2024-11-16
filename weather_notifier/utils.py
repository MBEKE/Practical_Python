import requests
from config import API_KEY, BASE_URL

def fetch_weather(city):
    """
    Fetch weather data for a specific city using WeatherAPI.
    """
    try:
        params = {"key": API_KEY, "q": city}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error: City '{city}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def parse_weather_data(data):
    """
    Parse and display weather data from the API response.
    """
    if data:
        city = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Weather in {city}, {region}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition}")
    else:
        print("Could not retrieve weather data.")
