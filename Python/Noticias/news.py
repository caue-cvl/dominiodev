import dia_de_hoje
import temperatura_local
import dolar

def bordas():
    print('-'*90)

def programa_principal():
    bordas()
    dia_de_hoje.mostrar_dia()
    bordas()
    temperatura_local.mostrar_temperatura_do_dia()
    bordas()
    dolar.mostrar_dolar_para_real()
    bordas()
programa_principal()
