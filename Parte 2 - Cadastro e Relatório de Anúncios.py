#Parte 2 - Cadastro e Relatório de Anúncios

import time

diasEmCadaMes = {1:31,
             2:28,
             3:31,
             4:30,
             5:31,
             6:30,
             7:31,
             8:31,
             9:30,
            10:31,
            11:30,
            12:31}

def metricas(valorInvestido):

    quantidadesMaximas = []
    
    viewsAtuais = 30*valorInvestido
    totalViews = viewsAtuais
    totalShares = 0
    totalClicks = 0

    for i in range (4):

        clicksAtuais = viewsAtuais*0.12
        sharesAtuais = clicksAtuais*0.15
        viewsAtuais = sharesAtuais*40
        
        totalViews += viewsAtuais
        totalClicks += clicksAtuais
        totalShares += sharesAtuais

    quantidadesMaximas.append(totalViews)
    quantidadesMaximas.append(totalClicks)
    quantidadesMaximas.append(totalShares)

    return quantidadesMaximas

def numero_anos_bissextos(anoGenerico):
        
    anosDecorridos = anoGenerico - 1952
        
    if(anosDecorridos<0):
        numeroDeBissextos = 0 
        
    else:
        numeroDeBissextos = int(anosDecorridos / 4)
        numeroDeBissextos += 1
            
    return numeroDeBissextos

def numero_dias_meses_anteriores(mesGenerico, decadaGenerica):

    dias = 0

    for mes in range(mesGenerico-1):
            dias += diasEmCadaMes[mes+1]
    
    
    if (not (decadaGenerica%4) and mesGenerico>2):
        dias += 1

    return dias

def converterDataParaDias(dataGenerica):

    diaGenerico = int(dataGenerica[0:2:])
    mesGenerico = int(dataGenerica[3:5:])
    anoGenerico = int(dataGenerica[6:10:])
    decadaGenerica = int(dataGenerica[8:10])
        
    anosAnteriores = anoGenerico - 1950
    diasExtrasDeAnosBissextos = numero_anos_bissextos(anoGenerico-1)
    diasDosMesesPassados = numero_dias_meses_anteriores(mesGenerico, decadaGenerica)

    dias = anosAnteriores*365 + diasExtrasDeAnosBissextos + diasDosMesesPassados + diaGenerico

    return dias

def transformarNumeroEmLista(numero):

    lista = []
    
    for Item in range (numero):
        lista.append(Item)

    return lista

def filtroPorCliente(nAnunciosRegistrados, nomesDosClientes):

    listaIndices = []
    listaFiltro = transformarNumeroEmLista(nAnunciosRegistrados)   

    nomeRefCliente = input("Digite o nome do cliente a ser encontrado:\t")
    
    for var in listaFiltro:

        if nomesDosClientes[var] == nomeRefCliente:
            listaIndices.append(var)

    return listaIndices

def filtroPorData(nAnunciosRegistrados, datasDeInicio, datasDeTermino, nomesCliente, doisFiltros):
    
    listaIndicesInicio = []
    listaIndices = []
    
    if doisFiltros:
        listaFiltro = filtroPorCliente(nAnunciosRegistrados, nomesCliente) #lista

    else:
        listaFiltro = transformarNumeroEmLista(nAnunciosRegistrados) #lista

    dataRefInicioEmDias = converterDataParaDias(input("\nDigite a data de início do intervalo desejado:\t"))
    dataRefFinalEmDias = converterDataParaDias(input ("\nDigite a data de término do intervalo desejado:\t"))

    for var1 in listaFiltro:

        if converterDataParaDias(datasDeInicio[var1]) >= dataRefInicioEmDias:
            listaIndicesInicio.append(var1)

    for var2 in listaIndicesInicio:
        if converterDataParaDias(datasDeTermino[var2]) <= dataRefFinalEmDias:
            listaIndices.append(var2)

    return listaIndices


repetir = "S"

cadastros = 0

nomesAnuncio = []
nomesCliente = []
datasDeInicio = []
datasDeTermino = []
investimentosPorDia = []

while (not (repetir == "n" or repetir == "N")):
        
    tarefa = int(input("\nEscolha o procedimento a ser realizado:\n1 - Cadastrar dados de anúncio \n2 - Relatório dos anúncios cadastrados\n"))

    if tarefa == 1:
     
        print("\nVocê escolheu a tarefa 1. Vamos cadastrar o seu anúncio.")
            
        nomesAnuncio.append(input("\nDigite o título do anúncio:\t"))
        print("\nAnúncios: ", nomesAnuncio)

        nomesCliente.append(input("\nDigite o nome do cliente que está anunciando:\t"))

        datasDeInicio.append(input("\nDigite a data de início do investimento:\t"))

        datasDeTermino.append(input("\nDigite a data de término do investimento:\t"))

        investimentosPorDia.append(int(input("\nDigite o valor do investimento diário (em reais):\t")))
           
        cadastros += 1

    elif tarefa == 2:

        if(cadastros):
        
            filtro = input("\nVocê escolheu a tarefa 2. Deseja filtrar os anúncios por intervalo de tempo e/ou cliente? S-sim, N-não:\t")

            if (not (filtro == "n" or filtro == "N")):

                print("\nOs dados serão filtrados.\n")
                
                tipoFiltro = int(input("\nEscolha o tipo de filtro desejado: \n1 - Por cliente  \n2 - Por intervalo de tempo \n3 - Ambos\n"))

                if tipoFiltro == 1:

                    indicesFiltrados =  filtroPorCliente(cadastros, nomesCliente) 
                    
                elif tipoFiltro == 2:

                    indicesFiltrados = filtroPorData(cadastros, datasDeInicio, datasDeTermino, nomesCliente, False)

                elif tipoFiltro == 3:
                    
                    indicesFiltrados = filtroPorData(cadastros, datasDeInicio, datasDeTermino, nomesCliente, True)

                else:
                    print("\nOpção inválida.") 

            else:
                print("\nNenhum filtro foi aplicado.\n")
                indicesFiltrados = transformarNumeroEmLista(cadastros)

            print("\nNúmero de cadastros: ", cadastros)

            if (not indicesFiltrados):
                print("\nNenhum resultado encontrado.\n")

            else:

                for dados in indicesFiltrados:
                    
                    relatorio = metricas(investimentosPorDia[dados])
                
                    vtInvestido = investimentosPorDia[dados]*(converterDataParaDias(datasDeTermino[dados]) - converterDataParaDias(datasDeInicio[dados]))

                    print("\n\nTítulo: ", nomesAnuncio[dados], "\nCliente: ", nomesCliente[dados], "\nData de início do investimento: ", datasDeInicio[dados], "\nData de término do investimento: ", datasDeTermino[dados], "\nValor diário investido: ", investimentosPorDia[dados], "reais")
                    print("\n\nValor total investido: ", vtInvestido, "reais\nQuantidade máxima de visualizações: ", round(relatorio[0]), "\nQuantidade máxima de cliques: ", round(relatorio[1]), "\nQuantidade máxima de compartilhamentos: ", round(relatorio[2]))
        
        else:
            print("\nNão existem cadastros registrados.\n")

    else:
        print("\nOpção inválida.")        

    repetir = input("\nDeseja registrar ou obter mais anúncios? S-sim, N-não: ")

print("\nEncerrando...")
time.sleep(5)
