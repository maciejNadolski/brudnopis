from urllib import response
import requests
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import time


def get_coords():
     while True:
        address = input("Podaj adres: ")

        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q" : address,
            "limit" : 1,
            "countrycodes" : "pl",
            "format" : "jsonv2"
            }

        response = requests.get(url, params=params)
        data = response.json()

        if data:
            latitude = data['lat']
            longitude = data['lon']
            break
        else:
            print("Nie znaleziono adresu.")    

        return latitude,longitude


def get_station_imgw():
    url = "https://danepubliczne.imgw.pl/api/data/meteo"
    response = requests.get(url)
    data = response.json()

    while True:
        nazwa_stacji = input("Podaj nazwę stacji: ").strip().upper()
        if nazwa_stacji.lower() == "tu":
            nazwa_stacji = "WARSZAWA-OKĘCIE"
        nazwa_stacji = nazwa_stacji.upper()

        for item in data:
            if item['nazwa_stacji'] == nazwa_stacji:
                print(f"nazwa stacji: {item['nazwa_stacji']}")
                print(f"temperatura powietrza: {item['temperatura_powietrza']}")
                print(f"wiatr średnia prędkość: {item['wiatr_srednia_predkosc']}")
                print(f"wilgotność: {item['wilgotnosc_wzgledna']}")
                print(f"opady: {item['opad_10min']}")
                return item  
        print("Nie znaleziono stacji. Spróbuj ponownie.")
        print("========================================")

def get_station_openw():
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": 52.20248916962441, 
	"longitude": 21.02345981078115,
	"current": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation",
}
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]
    current = response.Current()
    temperature = current.Variables(0).Value()  
    wind = current.Variables(1).Value() *1000/3600
    humid = current.Variables(2).Value()
    rain = current.Variables(3).Value()

    print(f"Współrzędne: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elewacja: {response.Elevation()} m n.p.m.")
    print(f"Temperatura: {temperature:.2f}°C")
    print(f"Wiatr: {wind:.2f} m/s")
    print(f"Wilgotność: {humid:.2f}%")
    print(f"Opady: {rain:.2f}mm")


if __name__ == "__main__":
    get_coords()
    # print("Dane z IMGW:")
    # get_station_imgw()
    # print("========================================")
    # print("Dane z OpenWeatherMap:")
    # get_station_openw()

    #todo zrobić opcje wyboru współrzędnych z mapy
    #todo zrobić frontend w HTML i JS, który będzie wyświetlał dane w tabeli i umożliwiał wybór stacji z listy rozwijanej