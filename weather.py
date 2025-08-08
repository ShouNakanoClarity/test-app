import requests

def get_weather(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to retrieve weather data.")
    
    data = response.json()
    weather = data.get("current_weather", {})
    return {
        "temperature": weather.get("temperature"),
        "windspeed": weather.get("windspeed"),
        "weathercode": weather.get("weathercode"),
        "time": weather.get("time")
    }
