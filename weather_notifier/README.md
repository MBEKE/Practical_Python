Weather Notification Service
A simple command-line tool to fetch and display current weather information for any city using WeatherAPI.

Features
Fetches real-time weather data from WeatherAPI.
Displays temperature, weather condition, and location details.
Handles errors like invalid city names or network issues gracefully.
Setup Instructions
Prerequisites
Python 3.6 or later
A WeatherAPI account (sign up here to get your API key)
Internet connection
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/weather-notification-service.git
cd weather-notification-service
2. Install Dependencies
Install the requests library:

bash
Copy code
pip install requests
3. Set Up Your API Key
Open the config.py file.
Replace your_weatherapi_key_here with your WeatherAPI key:
python
Copy code
API_KEY = "your_weatherapi_key_here"
Usage
Run the program from the command line, providing the city name as an argument:

bash
Copy code
python3 main.py <city_name>
Example
bash
Copy code
python3 main.py Nairobi
Output:

yaml
Copy code
Weather in Nairobi, Nairobi, Kenya:
Temperature: 25°C
Condition: Partly cloudy
Project Structure
bash
Copy code
weather-notification-service/
│
├── config.py          # API key and endpoint configuration
├── utils.py           # Fetches and processes weather data
├── main.py            # Command-line interface
├── README.md          # Project documentation
└── __pycache__/       # Auto-generated Python cache files
Error Handling
The program handles:

Invalid City Names:
javascript
Copy code
Error: City 'InvalidCity' not found.
Could not retrieve weather data.
Network Issues:
javascript
Copy code
Error fetching weather data: <specific network error>
Future Enhancements
Add a feature to fetch multi-day weather forecasts.
Provide more detailed weather metrics like humidity, wind speed, etc.
Build a graphical user interface (GUI).
Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
WeatherAPI for providing the weather data API.
