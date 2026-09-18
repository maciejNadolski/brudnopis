
import requests

def get_timetable(url):
    response = requests.get(url)
    data = response.json()

    nazwa_stacji = input("Podaj nazwę stacji [caps]: ")
    if nazwa_stacji == "tu":
        nazwa_stacji = "WARSZAWA-OKĘCIE"
    
    while True:
        for item in data:
            if item['nazwa_stacji'] == nazwa_stacji:
                print(f"nazwa_stacji: {item['nazwa_stacji']}")
                print(f"temperatura powietrza: {item['temperatura_powietrza']}")
                print(f"wiatr średnia prędkość: {item['wiatr_srednia_predkosc']}")
                print(f"wilgotność: {item['wilgotnosc_wzgledna']}")
                print(f"opady: {item['opad_10min']}")
                return item
        print("Nie znaleziono stacji. Spróbuj ponownie.")
        nazwa_stacji = input("Podaj nazwę stacji [caps]: ")

if __name__ == "__main__":
    url = 'https://danepubliczne.imgw.pl/api/data/meteo/'

    dane = get_timetable(url)
    