# ESTRUTURA DE REPETIÇÃO DE SOMA E MÉDIA DE IDADE 
soma = 0
media = 0
maior_idade = 0
nome_maior = "" # STRING
for i in range (3):
    nome = input("Qual o seu nome? ")
    idade = int(input("Qual a sua idade? "))
    if idade > maior_idade:
        maior_idade = idade
        nome_maior = nome
    soma = soma + idade
media = soma / (i + 1) # I inicia com valor zero. Portanto é necessário adicionar +1
print(f"Soma da idade do grupo de pessoas é {soma} anos e a média da idade é {media:.0f} anos.")
print(f"{nome_maior} é a pessoa mais velha deste grupo com {maior_idade} anos!")
