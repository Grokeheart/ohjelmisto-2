import requests

paikkakunta = input("Syötä paikkakunta: ")

api_key = ""

res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&limit=1&appid={api_key}").json()

print(res["weather"][0]["description"])
print(res["main"]["temp"] - 273.15)
