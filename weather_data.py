import requests
from datetime import datetime
import pytz

TZ = pytz.timezone("Asia/Tashkent")

API_TOKEN = "159e658ff15d308b63cff376abcf2838"

def get_weather_data(city_name: str) -> str:
    URL = f"https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {
        "appid": API_TOKEN,
        "q": city_name,
        "units": "metric",
    }
    weather_data = requests.get(url=URL, params=PARAMS)
    data = weather_data.json()

    if data["cod"] == 200:
        harorat = data['main']['temp']
        text = f"Bugun <b>{data['name']}</b> da\n\n"

        text += f"Harorat: <b>{harorat} °C</b>\n"
        text += f"Min. harorat: <b>{data['main']['temp_min']} °C</b>\n"
        text += f"Maks. harorat: <b>{data['main']['temp_max']} °C</b>\n\n"
        text += f"Bosim: <b>{data['main']['pressure']} Pa</b>\n"
        text += f"Namlik: <b>{data['main']['humidity']} %</b>\n"
        text += f"Shamol tezligi: <b>{data['wind']['speed']} m/s</b>\n\n"
        text += f"Quyosh chiqish vaqti: <b>{datetime.fromtimestamp(data['sys']['sunrise']).replace(tzinfo=pytz.utc).astimezone(TZ).strftime('%Y-%m-%d %H:%M:%S')}</b>\n"
        text += f"Quyosh botish vaqti: <b>{datetime.fromtimestamp(data['sys']['sunset']).replace(tzinfo=pytz.utc).astimezone(TZ).strftime('%Y-%m-%d %H:%M:%S')}</b>\n\n"
        if harorat < 10 :
            text += "<b>Issiqroq kiyinishingizni masalahat beraman</b>"
        return text
    else:
        return None