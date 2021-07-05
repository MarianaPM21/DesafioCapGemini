#Parte 1 - Calculadora de alcance de anúncio online

#Métricas

#A cada 100 pessoas que visualizam o anúncio, 12 clicam nele
#A cada 20 pessoas que clicam no anúncio, 3 compartilham nas redes sociais
#Cada compartilhamento nas redes sociais gera 40 novas visualizações
#30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido
#O mesmo anúncio é compartilhado no máximo 4 vezes em sequência (1ª pessoa --> compartilha --> 2ª pessoa --> compartilha --> 3ª pessoa --> compartilha --> 4ª pessoa )

import time

repetir = "S"

while not (repetir == "n" or repetir == "N"):

    valorInvestido = int(input("\nDigite o valor, em reais, a ser investido no anúncio: "))

    viewsAtuais = 30*valorInvestido
    totalViews = 0

    for i in range (4):

        totalViews += viewsAtuais
        print("\ntotalViews: ", totalViews)

        viewsAtuais *= 0.12*0.15*40
        print("\nviewsAtuais: ", viewsAtuais)

    print("\n\nA quantidade máxima aproximada de alcance desse investimento é de", round(totalViews), "pessoas.\n")

    repetir = input("\nDeseja calcular a projeção para mais um investimento? S-sim, N-não: ")
    
print("\nEncerrando...")
time.sleep(2)