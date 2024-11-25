# CALCULE SUA IDADE
import datetime #Importa a biblioteca datetime
nasc =  int(input("Infrome o ano de nascimento:"))
data_atual = datetime.date.today() #Armazena a data completa
ano_atual = data_atual.year #Armazena na variável o ano atual
idade = ano_atual - nasc
print(f"A sua idade é: {idade} anos!")
