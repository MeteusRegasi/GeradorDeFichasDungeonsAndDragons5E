def mostrarLinha(num=60):
    print('-' * num)
def titulo(msg, tamanho=60):
    mostrarLinha(tamanho)
    print(f'{msg:^60}'.upper())
    mostrarLinha(tamanho)
def valorInvalido():
    print('Valor inválido! Tente novamente!')
def checar(itemComparado, itemComparador, semMensagem=False):
    """
    -> pega um valor e compara a uma lista, se o valor estiver retorna 0, se não estiver retorna 1
    """
    valorValidoOuInvalido = 0
    for c in itemComparador:
        valorValidoOuInvalido += 1
        if c == itemComparado:
            valorValidoOuInvalido -= len(itemComparador)
    if valorValidoOuInvalido != 0 and semMensagem == False:
        valorInvalido()
    return valorValidoOuInvalido
def setinha():
    return input('-> ').strip().lower()
def querContinuar(msg):
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