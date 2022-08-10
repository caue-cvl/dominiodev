from datetime import date
import datetime
import constantes

def mostrar_dia():
    dia_semana = date.today().weekday()
    nomes = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")

    current_time = datetime.datetime.now()
    dia_de_hoje = f'{current_time.day}/{current_time.month}/{current_time.year}'
    print(f'Hoje é {nomes[dia_semana]} dia {constantes.BOLD}{dia_de_hoje}{constantes.RESET}')
    return dia_de_hoje