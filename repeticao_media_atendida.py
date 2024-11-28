# CALCULO DE MEDIA ATENTIDA
for i in range(3):
    nome = str(input("Qual o nome do estudante? "))
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    media = (nota1 + nota2) / 2 
    if media >= 7:
        print(f"{nome}, você está APROVADO! Sua média é: {media}")
    elif media >=3:
         print(f"{nome}, você está EM RECUPERAÇÃO! Sua média é: {media}")
    else:
        print(f"{nome}, você está REPROVADO! Sua média é: {media}")
