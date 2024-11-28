# MÉDIA ESCOLAR COM CRITÉRIOS
nome = input( "Qual seu nome? ")
nota_1 = float(input( "Qual a nota da primeira avaliação? "))
nota_2 = float(input( "Qual a nota da segunda avaliação? "))
nota_3 = float(input( "Qual a nota da terceira avaliação? "))
media = float(nota_1 + nota_2 + nota_3) / 3
if media >= 6:
    print(f"Sr(a) {nome}, sua média é {media:.2f}. Você foi: APROVADO!")
else:
    print(f"Sr(a) {nome}, sua média é {media:.2f}. Você foi: REPROVADO!") 
    