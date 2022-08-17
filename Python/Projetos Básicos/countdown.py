import time

def definir_contagem():
    tempo = int(input("Tempo em segudos: "))
    cont = 0
    if cont != 0:
        return
    else:
        cont += 1
        return tempo

def contagem_regressiva(tempo):
    for regressiva in range (-1, tempo):
        if tempo > 0:
            print(tempo)
            time.sleep(1)
            tempo = tempo - 1
        else:
            print('BOOM!!!')
    return tempo

def executar():
    contagem_regressiva(definir_contagem())


executar()