# PESO IDEAL COM CRITÉRIOS
nome = input("Qual seu nome? ")
altura = float(input("Qual a sua altura? "))
sexo = str(input("HOMEM ou MULHER? "))
if sexo == "HOMEM":
    PiH = (72.7 * altura) - 58
    print(f"O peso ideal para você é de {PiH:.2f} Kg ")
else:
    PiM = (62.1 * altura) - 47.7
    print(f"O peso ideal para você é de {PiM:.2f} Kg ")
    