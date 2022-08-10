import constantes
import requests
import json


def localizador_cidade():
    geo_req = requests.get(constantes.base_url_localizador)
    geo_json = json.loads(geo_req.text)
    city = geo_json['city']
    return city


def consultar_api():
        city = localizador_cidade()
        base_url_weather = "http://api.openweathermap.org/data/2.5/weather?appid=" + constantes.API_key_weather + "&q=" + city + "&units=metric"
        weather_data = requests.get(base_url_weather).json()
        return weather_data


def mostrar_temperatura():
        temperatura_geral = consultar_api()
        temperatura_dia = temperatura_geral['main']['temp']
        temperatura_minima = temperatura_geral['main']['temp_min']
        temperatura_maxima = temperatura_geral['main']['temp_max']
        print(f"Segue temperatura da cidade {constantes.BOLD}{temperatura_geral['name']}{constantes.RESET}")
        print(f"Média  de:{constantes.YELLOW}", round(float(temperatura_dia)), f"°C {constantes.RESET}")
        print(f"Máxima de:{constantes.RED}", round(float(temperatura_maxima)), f"°C{constantes.RESET}")
        print(f"Mínima de:{constantes.CYAN}", round(float(temperatura_minima)), f"°C{constantes.RESET}")
def mostrar_temperatura_do_dia():
    mostrar_temperatura()