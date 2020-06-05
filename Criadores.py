from ComandosUteis import *
from ValoresPadroes import *


#Pega o valor das variáveis pré definidas
atributosAbreviaçãoPadrao = variaveis()[1]
idiomasPossiveis = variaveis()[2]
tendênciasPossiveis = variaveis()[3]
tiposDeEquipamentos = variaveis()[7]
propriedadeDasArmas = variaveis()[8]
tiposDeArmas = variaveis()[9]
tiposDeDados = variaveis()[10]
tiposDeDano = variaveis(11)



def criarRaca():
    #Dicionário onde ficarão as características da classe.
    caracteristicasDeRaca = {}

    """#----------------------------------NOME----------------------------------
    while True:
        caracteristicasDeRaca["nome"] = input('Digite o nome da raça: ').strip().title()
        if caracteristicasDeRaca["nome"].isalpha() == False:
            valorInvalido
        else:
            break
    mostrarLinha()

    #----------------------------------DESOLCAMENTO----------------------------------
    print('Informe o deslocamento em metros.')   
    caracteristicasDeRaca['deslocamento'] = eDecimal(' metros')
    mostrarLinha()

    #----------------------------------PESO----------------------------------
    print('Informe o peso média da raça em Kg.')
    caracteristicasDeRaca['peso'] = eDecimal('kg')
    mostrarLinha()

    #----------------------------------IDADE----------------------------------
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

    #----------------------------------ALTURA MÉDIA----------------------------------
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

    #----------------------------------AJUSTES DE ATRIBUTO----------------------------------
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

    #----------------------------------TENDÊNCIAS----------------------------------
    #Texto mostrando as tendências possíveis
    print(f'Selecione a tendência: {mostrarLista(tendenciasPossiveis)}')
    #Checa se a tendência digitada está correta, se não, repete
    while True:
        minhaTendencia = setinha()
        validoOuInvalido = checar(minhaTendencia, tendenciasPossiveis)
        if validoOuInvalido == 0:
            break
    #Define a tendência normal da raça
    caracteristicasDeRaca['tendência'] = minhaTendencia
    mostrarLinha()

    #----------------------------------IDIOMA----------------------------------
    print(f'Digite o idioma da sua classe. Possibilidades: {mostrarLista(idiomasPossiveis)}')
    meusIdiomas = []
    while True:
        escolhaIdioma = setinha()
        validoOuInvalido = checar(escolhaIdioma, idiomasPossiveis)
        if validoOuInvalido == 0:
            validoOuInvalido = checar(escolhaIdioma, meusIdiomas, semMensagem=True, inverter=True)
            if validoOuInvalido == 1 and meusIdiomas != []:
                print('Idioma já registrado!')
            else:
                meusIdiomas.append(escolhaIdioma)
                escolhaMaisIdiomas = querContinuar('Deseja adicionar mais um idioma?')
                if escolhaMaisIdiomas == 'n':
                    break
    caracteristicasDeRaca['idiomas'] = meusIdiomas
    mostrarLinha()

    #----------------------------------HABILIDADES----------------------------------
    minhasHabilidades = []
    while True:
        validoOuInvalido = 0
        validoOuInvalido = querContinuar('Deseja adicionar uma habilidade?')
        if validoOuInvalido == 's':
            adicionarHabilidade = {}
            nomeDaHabilidade = input('-Nome: ')
            adicionarHabilidade[nomeDaHabilidade] = input('-Características: ')
            minhasHabilidades.append(adicionarHabilidade)
            mostrarLinha()
        else:
            mostrarLinha()
            break
    if minhasHabilidades != []:
        caracteristicasDeRaca['habilidades'] = minhasHabilidades
    
    #----------------------------------PROFICIÊNCIA----------------

    
    #----------------------------------MAGIA----------------------------------
    
    #----------------------------------SUBRAÇA----------------------------------
    
    #----------------------------------SALVANDO A RAÇA----------------------------------

    return caracteristicasDeRaca"""
    

def criarEquipamento():
    caracteristicasDoEquipamento = {}

    #Define o nome do equipamento
    print('Informe o nome do equipamento: ')
    caracteristicasDoEquipamento['nome do equipamento'] = setinha()
    mostrarLinha()

    #Define o tipo de equipamento
    print('Digite o tipo de equipamento(arma, armadura ou item): ')
    while True:
        tipoDoEquipamento = setinha()
        valorValidoOuInvalido = checar(tipoDoEquipamento, tiposDeEquipamentos, semMensagem=True)
        if valorValidoOuInvalido != 0:
            valorInvalido()
        else:
            caracteristicasDoEquipamento['tipo do equipamento'] = tipoDoEquipamento
            break
    mostrarLinha()

    #----------------------------------ARMAS----------------------------------
    if tipoDoEquipamento == 'arma':
        #Define o tipo de arma
        print(f'Selecione o tipo de arma: {mostrarLista(tiposDeArmas)}')
        while True:
            tipoDeArmaEscolhido = setinha()
            valorValidoOuInvalido = checar(tipoDeArmaEscolhido, tiposDeArmas, semMensagem=True)
            if valorValidoOuInvalido == 0:
                break
            else:
                valorInvalido()
        mostrarLinha()

        #Define o dano da arma e o tipo de dano
        print(f'Indique o dado de dano da arma junto do tipo de dano. Ex: 1d12 concussão, 1d6 cortante ou 1d4 perfurante\nDados: {mostrarLista(tiposDeDados)}\n Dano: {mostrarLista(tiposDeDano)}')


        #Define as propriedades da arma
        listaDePropriedadesDaArma = []
        print(f'Escolha as propriedades de sua arma({mostrarLista(propriedadeDasArmas)}).')
        while True:
            #Checa se não é uma propriedade ou se repete
            propriedadeDaArma = setinha()
            valorValidoOuInvalido = checar(propriedadeDaArma, propriedadeDasArmas, semMensagem=True)
            if valorValidoOuInvalido == 0:
                valorValidoOuInvalido = checar(propriedadeDaArma, listaDePropriedadesDaArma, semMensagem=True, inverter=True)
                if valorValidoOuInvalido == 0:
                    #Propriedades especiais
                    if propriedadeDaArma == 'arremesso':
                        print('Indique a distância mínima e máxima do arremesso(em metros): ')
                        while True:
                            print('-Mínima:')
                            distanciaMinimaArremesso = setinha()
                            print('-Máxima:')
                            distanciaMaximaArremesso = setinha()
                            if distanciaMaximaArremesso.isnumeric() == True and distanciaMinimaArremesso.isnumeric() == True:
                                propriedadeDaArma = f'arremesso({distanciaMinimaArremesso}/{distanciaMaximaArremesso})'
                                break
                            else:
                                valorInvalido()
                    elif propriedadeDaArma == 'versátil':
                        print(f'Indique o segundo dado de dano da arma({tiposDeDados}): ')
                        while True:
                            segundoDadoDeDano = setinha()
                            valorValidoOuInvalido = identificarDado(segundoDadoDeDano)
                            if valorValidoOuInvalido == 0:
                                propriedadeDaArma = f'versátil({segundoDadoDeDano})'
                                break
                            else:
                                valorInvalido()
                    elif propriedadeDaArma == 'especial':
                        print('Indique a propriedade: ')
                        propriedadeDaArma = {'especial':setinha()}
                    listaDePropriedadesDaArma.append(propriedadeDaArma)
            if valorValidoOuInvalido != 0:
                valorInvalido()
            #Pergunta se quer continuar
            else: 
                valorValidoOuInvalido = querContinuar('Deseja adicionar mais alguma propriedade?')
                if valorValidoOuInvalido == 'n':
                    break
        caracteristicasDoEquipamento['propriedades'] = listaDePropriedadesDaArma
        mostrarLinha()

    #----------------------------------ARMADURAS----------------------------------
    elif tipoDoEquipamento == 'armadura':
        print('Qual o nome da armadura?')
        caracteristicasDoEquipamento['nome do equipamento'] = setinha()

    #----------------------------------ÍTENS----------------------------------
    else: 
        print('Qual o nome do item?')
        caracteristicasDoEquipamento['nome do equipamento'] = setinha()
        
    return caracteristicasDoEquipamento
    

print(criarEquipamento())