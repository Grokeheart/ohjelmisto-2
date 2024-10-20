import requests

paikkakunta = input("Syötä paikkakunta: ")

api_key = "5ee562d3cae1a968b23b545d0959a16c"

res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&limit=1&appid={api_key}").json()

print(res["weather"][0]["description"])
print(res["main"]["temp"] - 273.15)