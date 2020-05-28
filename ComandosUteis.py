def mostrarLinha(num=60):
    print('-' * num)
def titulo(msg, tamanho=60):
    mostrarLinha(tamanho)
    print(f'{msg:^60}'.upper())
    mostrarLinha(tamanho)
def valorInvalido():
    print('Valor inválido! Tente novamente!')