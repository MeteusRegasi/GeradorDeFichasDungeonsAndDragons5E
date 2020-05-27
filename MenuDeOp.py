from ComandosUteis import *


def chamarMenu():
    listaDePossiveisEscolhas = [1, 2, 3]
    Titulo
    while True:
        escolha = input("""
        Selecione a sua opção:
        1) Gerar ficha aleatória
        2) Gerar ficha semi-aleatória
        3) Mostrar fichas
        -> """)
        if escolha.isnumeric() == False or escolha not in listaDePossiveisEscolhas:
            print('Opção inválida! Selecione novamente!')
        else:
            break
    return escolha