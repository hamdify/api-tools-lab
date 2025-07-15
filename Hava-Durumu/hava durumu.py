import requests

def get_coords():
    while True:
        city = input("Hangi şehrin hava verilerini görmek istersiniz? ").strip().lower()
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": city,
            "format": "jsonv2",
            "limit": 1,
            "countrycodes": "tr"
        }
        headers = {
            "User-Agent": "my-weather-app"
        }

        response = requests.get(url, params=params, headers=headers)
        print(f"→ Nominatim yanıt kodu: {response.status_code}")
        data = response.json()

        if not data:
            print("❌ Şehir bulunamadı. Lütfen tekrar deneyin.\n")
            continue

        display_name = data[0]["display_name"]
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        return lat, lon, display_name

while True:
    lat, lon, display_name = get_coords()

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "forecast_days": 1
    }
    headers = {
        "User-Agent": "my-weather-app"
    }

    response = requests.get(url, params=params, headers=headers)
    print(f"→ Open-Meteo yanıt kodu: {response.status_code}")
    data = response.json()

    if "hourly" not in data or "temperature_2m" not in data["hourly"]:
        print("❌ Bu şehir için hava verisi alınamadı. Lütfen başka bir şehir deneyin.")
        continue

    times = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]


    print(f"\n📍 {display_name} şehri için saatlik sıcaklık verileri:\n")
    for time, temp in zip(times, temps):
        print(f"{time} → {temp} °C")

    devam = input("\nYeni bir şehir sorgulamak için enter'a basın.\nÇıkmak için 'q' yazın: ")
    if devam.strip().lower() == "q":
        break
