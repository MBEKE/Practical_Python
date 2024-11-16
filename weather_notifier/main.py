import argparse
from utils import fetch_weather, parse_weather_data

def main():
    """
    Main function to handle command-line arguments and fetch weather data.
    """
    parser = argparse.ArgumentParser(description="Weather Notification Service using WeatherAPI")
    parser.add_argument("city", help="City name to get the weather for")
    args = parser.parse_args()

    city = args.city
    data = fetch_weather(city)
    parse_weather_data(data)

if __name__ == "__main__":
    main()
