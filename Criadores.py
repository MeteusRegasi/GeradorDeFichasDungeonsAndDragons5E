from ComandosUteis import *
from ValoresPadroes import *


#Pega o valor das variáveis de abreviações de atributos e coloca na variável
atributosAbreviaçãoPadrao = variaveis()[1]
idiomasPossiveis = variaveis()[2]



def criarRaca():
    #Dicionário onde ficarão as características da classe.
    caracteristicasDeRaca = {}

    #-----------------Nome-----------------
    while True:
        caracteristicasDeRaca["nome"] = input('Digite o nome da raça: ').strip().title()
        if caracteristicasDeRaca["nome"].isalpha() == False:
            valorInvalido
        else:
            break
    mostrarLinha()

    #-----------------Ajustes de atributo-----------------
    print("""Ajuste de atributo: digite o valor que você quer adicionar em seguida a abreviação do atributo(3 primeiras letras).
Ex: 2 des 1 for""")
    mostrarLinha()
    atributosDeRaca = {}
    #Checa os valores e atributos
    while True:
        validoOuInvalido = 0
        ajustesAtributos = input('-> ').lower().strip().split()
        #Checa se tem mais de uma palavras
        if len(ajustesAtributos) >= 2:
            #Checa os números
            for c1 in range(0, len(ajustesAtributos), 2):
                if ajustesAtributos[c1].isnumeric() == False:
                    validoOuInvalido = -1
                    break
            #Se não estiver errado, checa as abreviações dos atributos
            if validoOuInvalido == 0:
                for c2 in range(1, len(ajustesAtributos) + 1, 2):
                    validoOuInvalido = 0
                    for itens1 in atributosAbreviaçãoPadrao:
                        validoOuInvalido += 1
                        if itens1 == ajustesAtributos[c2]:
                            validoOuInvalido -= len(atributosAbreviaçãoPadrao)
                    if validoOuInvalido != 0:
                        break
        else:
            validoOuInvalido = -1
        #Se o número do válido ou inválido for diferente de 0 vai repetir
        if validoOuInvalido == 0:
            break
        else:
            valorInvalido()
    #Adiciona o valor em cada determinado atributo
    for atributo in atributosAbreviaçãoPadrao:
        atributosDeRaca[atributo] = 0
        for c3 in range(1, len(ajustesAtributos), 2):
            if ajustesAtributos[c3] == atributo:
                atributosDeRaca[atributo] = f'+{ajustesAtributos[c3 - 1]}'
    caracteristicasDeRaca['ajustes de atributo'] = atributosDeRaca
    mostrarLinha()

    #-----------------Tendências-----------------
    #Texto mostrando as tendências possíveis
    print("""Selecione a tendência: leal e bom, leal e neutro, leal e mau, neutro e bom, neutro e neutro, neutro e caótico, caótico e bom, caótico e neutro ou caótico e mau.""")
    #Checa se a tendência digitada está correta, se não, repete
    while True:
        validoOuInvalido = 0
        minhaTendencia = input('-> ').lower().strip()
        for tendencia in variaveis()[3]:
            validoOuInvalido += 1
            if tendencia == minhaTendencia:
                validoOuInvalido -= len(variaveis()[3])
        if validoOuInvalido != 0:
            valorInvalido()
        else:
            break
    #Define a tendência normal da raça
    caracteristicasDeRaca['tendência'] = minhaTendencia
    mostrarLinha()

    #-----------------Idioma-----------------
    print('Digite o idioma da sua classe. Possibilidades: todos os idiomas e um a escolha')
    meusIdiomas = []
    while True:
        validoOuInvalido = 0
        escolhaIdioma = input('-> ').strip().lower()
        for idioma in idiomasPossiveis:
            validoOuInvalido += 1
            if idioma == escolhaIdioma:
                validoOuInvalido -= len(idiomasPossiveis)
        if validoOuInvalido != 0:
            valorInvalido()
        else:
            meusIdiomas.append(escolhaIdioma)
            while True:
                escolhaMaisIdiomas = input('Deseja adicionar mais um idioma?[s/n]').lower().strip()[0]
                if escolhaMaisIdiomas == 's' or escolhaMaisIdiomas == 'n':
                    break
            if escolhaMaisIdiomas == 'n':
                break
    caracteristicasDeRaca['idiomas'] = meusIdiomas

    return caracteristicasDeRaca

print(criarRaca())