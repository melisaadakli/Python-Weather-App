import requests

def weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can also use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\nWeather Information - {city}")
            print("------------------------")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
            print(f"Description: {data['weather'][0]['description']}")
        else:
            print(f"Unable to fetch weather information. Error Code: {data['cod']} - {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = "openweatherapp_api_key"
    city = input("Please enter the city for weather information: ")
    
    weather(api_key, city)
