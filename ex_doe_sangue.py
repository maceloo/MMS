# DOAÇÃO DE SANGUE
idade = int(input("Informe a sua idade:"))
peso = float(input("Informe seu peso em Kg:"))
sono = int(input("Informe a quantidade de horas de sono:"))
if (idade >= 16 and idade <=69):
    if peso >= 50:
        if sono >= 6:    
            print("Você está apto para doar sangue")
        else:
            print("Você não está apto para doar sangue, pois não dormiu o suficiente!")   
    else:
     print("Você não está apto para doar sangue, pois não peso o suficiente!")
else:        
 print("Você não está apto para doar sangue, pois não idade suficiente!")
