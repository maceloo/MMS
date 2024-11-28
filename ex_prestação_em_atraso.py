#PRESTAÇÃO EM ATRASO
Prestacao = float(input("Informe o valor da sua prestação:"))
Taxa = float(input("Qual a taxa de juros aplicada?"))
Tempo = float(input("Quantos meses está em atraso?"))
Valor_final = Prestacao+(Prestacao*(Taxa/100)*Tempo)
print(f"O Valor final da prestação é R$ {Valor_final:.2f}")
