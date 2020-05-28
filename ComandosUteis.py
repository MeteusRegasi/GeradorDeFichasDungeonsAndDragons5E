def mostrarLinha(num=60):
    print('-' * num)
def titulo(msg, tamanho=60):
    mostrarLinha(tamanho)
    print(f'{msg:^60}'.upper())
    mostrarLinha(tamanho)
def valorInvalido():
    print('Valor inválido! Tente novamente!')
def checar(itemComparado, itemComparador):
    valorValidoOuInvalido = 0
    for c in itemComparador:
        valorValidoOuInvalido += 1
        if c == itemComparado:
            valorValidoOuInvalido -= len(itemComparador)
    if valorValidoOuInvalido != 0:
        valorInvalido()
    return valorValidoOuInvalido
        