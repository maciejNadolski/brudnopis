import requests
from bs4 import BeautifulSoup
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
mk_ird = {
    '1u1': 'https://8.8.8.8', '1u2': 'https://8.8.8.8', '1u3': 'https://8.8.8.8', '1u4': 'https://8.8.8.8',
    '2u1': 'https://8.8.8.8', '2u2': 'https://8.8.8.8', '2u3': 'https://8.8.8.8', '2u4': 'https://8.8.8.8',
    '3u1': 'https://8.8.8.8', '3u2': 'https://8.8.8.8', '3u3': 'https://8.8.8.8', '3u4': 'https://8.8.8.8',
    '4u1': 'https://8.8.8.8', '4u2': 'https://8.8.8.8', '4u3': 'https://8.8.8.8', '4u4': 'https://8.8.8.8',
    '5u1': 'https://8.8.8.8', '5u2': 'https://8.8.8.8', '5u3': 'https://8.8.8.8', '5u4': 'https://8.8.8.8',
    '6u1': 'https://8.8.8.8', '6u2': 'https://8.8.8.8', '6u3': 'https://8.8.8.8', '6u4': 'https://8.8.8.8',
    '7u1': 'https://8.8.8.8', '7u2': 'https://8.8.8.8', '7u3': 'https://8.8.8.8', '7u4': 'https://8.8.8.8',
    '8u1': 'https://8.8.8.8', '8u2': 'https://8.8.8.8', '8u3': 'https://8.8.8.8', '8u4': 'https://8.8.8.8',
    '9u1': 'https://8.8.8.8', '9u2': 'https://8.8.8.8', '9u3': 'https://8.8.8.8', '9u4': 'https://8.8.8.8',
    '10u1': 'https://8.8.8.8', '10u2': 'https://8.8.8.8', '10u3': 'https://8.8.8.8', '10u4': 'https://8.8.8.8',
    '11u1': 'https://8.8.8.8', '11u2': 'https://8.8.8.8', '11u3': 'https://8.8.8.8', '11u4': 'https://8.8.8.8',
    '12u1': 'https://8.8.8.8', '12u2': 'https://8.8.8.8', '12u3': 'https://8.8.8.8', '12u4': 'https://8.8.8.8',
    '13u1': 'https://8.8.8.8', '13u2': 'https://8.8.8.8', '13u3': 'https://8.8.8.8', '13u4': 'https://8.8.8.8',
    '14u1': 'https://8.8.8.8', '14u2': 'https://8.8.8.8', '14u3': 'https://8.8.8.8', '14u4': 'https://8.8.8.8',
}

def input_ird():
    while True:
        odbiornik = input("Wpisz nazwę odbiornika: ")
        if odbiornik in mk_ird:
            odbiornik = mk_ird[odbiornik]
            break
    print(f"Wybrano odbiornik: {odbiornik}")
    return odbiornik

def main(odbiornik):
    
    url = odbiornik
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    if response.status_code == 200:
        print("Success")
    soup.prettify()

    query=soup.find_all('div')
    n = 1
    for link in query:
       print(f"{n}. {link.text}")
       n += 1

    enter_add = input("Wpisz nowy adres: ")
    enter_src = input("Wpisz nowy src: ")
    enter_port = input("Wpisz nowy port: ")

    payload = {
        'name': enter_add,
        'src': enter_src,
        'port': enter_port
        }

    payload = {
            'name': enter_add}

    response = requests.get(url+'/query', headers=headers, params=payload)
    print(response.url)
    print(response.text)

if __name__ == "__main__":
    odbiornik = input_ird()
    main(odbiornik)