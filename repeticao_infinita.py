# ESTRUTURA DE REPETIÇÃO INFINITA
i = 0
resp = "S"
while resp == "S" or resp == "s":
    print(i)
    i += 1
    resp = input("Deseja continuar (S/N)? ")
