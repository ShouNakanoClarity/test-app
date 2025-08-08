from weather import get_weather

def main():
    print("🌍 Simple Weather CLI App")
    try:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
    except ValueError:
        print("❌ Invalid input. Latitude and longitude must be numbers.")
        return

    try:
        weather = get_weather(lat, lon)
        print("\n📊 Current Weather:")
        print(f"  Temperature: {weather['temperature']}°C")
        print(f"  Wind Speed:  {weather['windspeed']} km/h")
        print(f"  Weather Code: {weather['weathercode']}")
        print(f"  Time:        {weather['time']}")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
