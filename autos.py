# ROUBO E FURTOS DE AUTOMÓVEIS

# importação da biblioteca pandas
import pandas as pd

def formatar(valor):           # criando função para formatação dos resultados das listas
    return "{:.2f}%".format(valor)

# banco de dados
roubo = pd.Series([100, 90, 80, 120, 110, 90, 70])
furto = pd.Series([80, 60, 70, 60, 100, 50, 30])
recuperacao = pd.Series([70, 50, 60, 80, 100, 70, 50])

# somando roubos e furtos das series
soma = roubo + furto
print(f"ROUBOS E FURTOS NOS ÚLTIMOS 7 DIAS:")
print(soma)

# somando taxa de recuperação dos roubos 
taxa_recup = recuperacao / roubo
print(f"TAXA DE RECUPERAÇÃO DOS VEÍCULOS NOS ÚLTIMOS 7 DIAS:")
tr = (taxa_recup * 100).apply(formatar)
print(tr)

# somando todos os dados de uma série
print(f"TOTAL DE ROUBOS DE VEÍCULOS:")
soma_roubos = roubo.sum() #usando função sum para somar 
print(f"O total de veículos roubados na semana foi de: {soma_roubos} veículos")

print(f"\nTOTAL DE FURTOS DE VEÍCULOS:")
soma_furtos = furto.sum()
print(f"O total de veículos furtados na semana foi de: {soma_furtos} veículos")

print(f"\nTOTAL DE RECUPERAÇÃO DE VEÍCULOS:")
soma_recuperacoes = recuperacao.sum ()
print(f"O total de veículos recuperados na semana foi de: {soma_recuperacoes} veículos")

print(f"\nTAXA DE RECUPERAÇÃO DE VEÍCULOS:")
soma_taxa_recup = (recuperacao.sum() / roubo.sum() ) * 100
print(f"A taxa total das recuperações dos últimos 7 dias foi de: {soma_taxa_recup:.2f}%")
