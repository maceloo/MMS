# DOAÇÃO DE SANGUE
idade = int(input("Informe a sua idade: "))
peso = float(input("Informe seu peso em Kg: "))
sono = int(input("Informe a quantidade de horas de sono: "))
if (idade >= 16 and idade <=69) and (peso >=50) and (sono >= 6):  
    print("Você está apto para doar sangue")
else:        
    print("Você não está apto para doar sangue!")
