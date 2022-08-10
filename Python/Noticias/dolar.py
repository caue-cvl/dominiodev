import constantes
import requests

def mostrar_dolar_para_real():

    response = requests.get(constantes.base_url_dolar)
    corretagem_bruta = response.json()
    dolar_para_real = corretagem_bruta['conversion_rates']['BRL']
    print(f'O valor do dolar hoje é {constantes.RED}R${format(dolar_para_real, ".2f")}{constantes.RESET}')
    return dolar_para_real