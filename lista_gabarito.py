# GABARITO
gabarito = ["A", "B", "B", "D", "E"]
resposta = []
qnt_acerto = 0
qnt_erro = 0
for i in range(len(gabarito)):
    resposta.append(str(input("QUAL A OPÇÃO MARCADA? ")))
    if gabarito[i] == resposta[i]:
        qnt_acerto += 1
    else:
        qnt_erro += 1
print(f"Você acertou {qnt_acerto}")     
