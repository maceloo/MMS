# ESTRUTURA DE REPETIÇÃO DE SOMA E MÉDIA DE IDADE 
soma = 0
media = 0
maior_idade = 0
for i in range (10):
    nome = input("Qual o seu nome? ")
    idade = int(input("Qual a sua idade? "))
    if idade > maior_idade:
        maior_idade = idade
    soma = soma + idade
    media = soma / 10
print(f"Soma da idade do grupo de pessoas {soma} e a média da idade é {media:.0f}.")
print(f"A pessoa mais velha deste grupo tem {maior_idade} anos!")
