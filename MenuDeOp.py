from ComandosUteis import *


def chamarMenu():
    #Opções do menu
    listaDePossiveisEscolhas = [0, 1, 2, 3, 4, 5, 6]
    #Textinho do Menu
    titulo('Menu de Opções')
    print("""Selecione a sua opção:
    0) Sair
    1) Gerar ficha aleatória
    2) Gerar ficha semi-aleatória
    3) Mostrar fichas
    4) Adicionar raça
    5) Adicionar classe
    6) Adicionar item""")
    #Você seleciona a opção, se for inválida pede pra selecionar uma válida
    while True:
        escolha = -1
        try:
            escolha = int(input('-> '))
        except:
            escolha = -1
        finally:
            mostrarLinha()
        if escolha < 0 or escolha > listaDePossiveisEscolhas[-1]:
            escolha = -1
        if escolha == -1:
            print('Opção inválida! Selecione novamente!')
        else:
            break 
    #Retorna o número escolhido
    return escolha