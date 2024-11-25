# SOMA ENTRE 5 NÚEMROS INTEIROS E FORNECE O MAIOR VALOR
soma = 0
maior = 0
for i in range (5): #REPETIÇÃO DE NÚMEROS QUE DESEJA OBTER
    num = int(input("Informe o Valor: "))
    if num > maior:
        maior = num
    soma = soma + num #Acumulador
print(f"O Resultado da soma é: {soma}. O maior valor informado é: {maior}")
