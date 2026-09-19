
import requests

def get_timetable(url):
    response = requests.get(url)
    data = response.json()
    
    while True:
        nazwa_stacji = input("Podaj nazwę stacji: ").upper()
        if nazwa_stacji.lower() == "tu":
            nazwa_stacji = "WARSZAWA-OKĘCIE"
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

if __name__ == "__main__":
    url = 'https://danepubliczne.imgw.pl/api/data/meteo/'

    dane = get_timetable(url)


    #todo dodać drugie api i porównanie danych z dwóch źródeł, np. IMGW i OpenWeatherMap
    #todo zrobić frontend w HTML i JS, który będzie wyświetlał dane w tabeli i umożliwiał wybór stacji z listy rozwijanej
    