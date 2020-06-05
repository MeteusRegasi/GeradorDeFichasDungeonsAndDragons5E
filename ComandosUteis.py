from ValoresPadroes import *


def mostrarLinha(num=60):
    print('-' * num)
def titulo(msg, tamanho=60):
    mostrarLinha(tamanho)
    print(f'{msg:^60}'.upper())
    mostrarLinha(tamanho)
def valorInvalido():
    print('Valor inválido! Tente novamente!')
def checar(itemComparado, itemComparador, semMensagem=False, inverter=False):
    """
    -> pega um valor e compara a uma lista, se o valor estiver retorna 0, se não estiver retorna 1
    """
    valorValidoOuInvalido = 0
    if len(itemComparador) == 0:
        valorValidoOuInvalido = 1
    else:
        for c in itemComparador:
            valorValidoOuInvalido += 1
            if c == itemComparado:
                valorValidoOuInvalido -= len(itemComparador)
        if valorValidoOuInvalido != 0 and semMensagem == False:
            valorValidoOuInvalido = 1
            valorInvalido()
    if inverter == True:
        if valorValidoOuInvalido == 0:
            valorValidoOuInvalido = 1
        elif valorValidoOuInvalido == 1:
            valorValidoOuInvalido = 0
    return valorValidoOuInvalido
def setinha():
    return input('-> ').strip().lower()
def querContinuar(msg='Quer continuar?'):
    """
    -> Pergunta se o usuário quer continuar, se ele quiser retorna 's', se ele não quiser retorna 'n'
    """
    while True:
        escolha = input(f'{msg}[s/n] ').lower()[0]
        if escolha == 's' or escolha == 'n':
            break
        else:
            valorInvalido()
    return escolha
def eDecimal(medida):
    """
    -> retorna o valor que o usuário escolheu em decimal junto com a unidade de medida escolida
    """
    while True:
        validoOuInvalido = 0
        try:
            decimal = float(setinha())
        except:
            validoOuInvalido = 1
        if validoOuInvalido == 0:
            return f'{decimal:.2f}{medida}'
            break
        else:
            valorInvalido()
def identificarDado(dado):
    tiposDeDados = variaveis()[10]
    valorValidoOuInvalido = 1
    if checar(dado, tiposDeDados, semMensagem=True) == 0:
        valorValidoOuInvalido = 0
    elif len(dado) >= 3:
        if checar(dado[-3:], tiposDeDados, semMensagem=True) == 0:
            if dado[:-3].isnumeric() == True:
                if int(dado[:-3]) >= 1:
                    valorValidoOuInvalido = 0
        elif checar(dado[-2:], tiposDeDados, semMensagem=True) == 0:
            if dado[:-2].isnumeric() == True:
                if int(dado[:-2]) >= 1:
                   valorValidoOuInvalido = 0
    return valorValidoOuInvalido
def mostrarLista(lista, semPrintar=True):
    listaEmTexto = ''
    for c in lista:
        listaEmTexto = f'{listaEmTexto}{c}, '
    if semPrintar == False:
        print(listaEmTexto[:-2])
    return listaEmTexto[:-2]