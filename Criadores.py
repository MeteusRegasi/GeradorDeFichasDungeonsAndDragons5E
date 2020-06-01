from ComandosUteis import *
from ValoresPadroes import *


#Pega o valor das variáveis de abreviações de atributos e coloca na variável
atributosAbreviaçãoPadrao = variaveis()[1]
idiomasPossiveis = variaveis()[2]



def criarRaca():
    #Dicionário onde ficarão as características da classe.
    caracteristicasDeRaca = {}

    """#-----------------Nome-----------------
    while True:
        caracteristicasDeRaca["nome"] = input('Digite o nome da raça: ').strip().title()
        if caracteristicasDeRaca["nome"].isalpha() == False:
            valorInvalido
        else:
            break
    mostrarLinha()

    #-----------------Deslocamento-----------------
    print('Informe o deslocamento em metros.')   
    caracteristicasDeRaca['deslocamento'] = eDecimal(' metros')
    mostrarLinha()

    #-----------------Peso-----------------
    print('Informe o peso média da raça em Kg.')
    caracteristicasDeRaca['peso'] = eDecimal('kg')
    mostrarLinha()

    #-----------------Idade-----------------
    print('Indique a idade a qual fica adulto e até onde vivem. Ex: 18 100')
    while True:
        validoOuInvalido = 0
        idadeDaRaca = setinha().split()
        for c4 in idadeDaRaca:
            try:
                int(c4)
            except:
                validoOuInvalido -= 1
        if validoOuInvalido == 0:
            if len(idadeDaRaca) != 2:
                valorInvalido()
            else:
                break
        else:
            valorInvalido()
    idadeDaRaca = f'Adulto aos {idadeDaRaca[0]}. Vivem até {idadeDaRaca[1]}.'
    caracteristicasDeRaca['idade'] = idadeDaRaca
    mostrarLinha()

    #-----------------Altura média-----------------
    print('Informe a altura média em metros.')
    while True:
        validoOuInvalido = 0
        minhaAltura = setinha().split()
        minhaAlturaRevisada = []
        for c5 in range(0, len(minhaAltura)):
            try:
                minhaAlturaRevisada.append(float(minhaAltura[c5]))
            except:
                validoOuInvalido = 1
                break
            if c5 == 2:
                validoOuInvalido = 1    
                break
        if validoOuInvalido == 0:
            if len(minhaAlturaRevisada) == 1:
                minhaAlturaRevisada = f'Mede cerca de {minhaAlturaRevisada[0]:.2f} metros.'
            else:
                minhaAlturaRevisada = f'Mede entre {minhaAlturaRevisada[0]} e {minhaAlturaRevisada[1]} metros.'
            caracteristicasDeRaca['altura'] = (minhaAlturaRevisada)
            break            
        else:
            valorInvalido()
    mostrarLinha()

    #-----------------Ajustes de atributo-----------------
    print('Ajuste de atributo: digite o valor que você quer adicionar em seguida a abreviação do atributo(3 primeiras letras).\nEx: 2 des 1 for')
    mostrarLinha()
    atributosDeRaca = {}
    #Checa os valores e atributos
    while True:
        validoOuInvalido = 0
        ajustesAtributos = setinha().split()
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
    print('Selecione a tendência: leal e bom, leal e neutro, leal e mau, neutro e bom, neutro e neutro, neutro e caótico, caótico e bom, caótico e neutro ou caótico e mau.')
    #Checa se a tendência digitada está correta, se não, repete
    while True:
        minhaTendencia = setinha()
        validoOuInvalido = checar(minhaTendencia, variaveis()[3])
        if validoOuInvalido == 0:
            break
    #Define a tendência normal da raça
    caracteristicasDeRaca['tendência'] = minhaTendencia
    mostrarLinha()

    #-----------------Idioma-----------------
    print('Digite o idioma da sua classe. Possibilidades: todos os idiomas e um a escolha')
    meusIdiomas = []
    while True:
        escolhaIdioma = setinha()
        validoOuInvalido = checar(escolhaIdioma, idiomasPossiveis)
        if validoOuInvalido == 0:
            validoOuInvalido = checar(escolhaIdioma, meusIdiomas, semMensagem=True)
            if validoOuInvalido == 0 and meusIdiomas != []:
                print('Idioma já registrado!')
            else:
                meusIdiomas.append(escolhaIdioma)
                escolhaMaisIdiomas = querContinuar('Deseja adicionar mais um idioma?')
                if escolhaMaisIdiomas == 'n':
                    break
    caracteristicasDeRaca['idiomas'] = meusIdiomas
    mostrarLinha()"""

    return caracteristicasDeRaca

print(criarRaca())