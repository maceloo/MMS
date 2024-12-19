# RELATÓRIO VENDEDORES

import pandas as pd
def formatar(valor):
    return "{:.2f}%".format(valor)

# CRIANDO TABELA VENDEDOR
vendedores = [
    ["Maria", 800, 700, 1000, 900, 1200, 600, 600],
    ["João", 900, 500, 1100, 1000, 900, 500, 700],
    ["Manuel", 700, 600, 900, 1200, 900, 700, 400]
]

# CRIANDO AS COLUNAS DA TABELA VENDEDOR
colunas = ["Nome","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho"]

# CRIANDO DATAFRAME VENDEDORES 
df_vendedores = pd.DataFrame(vendedores,columns=colunas)

# EXIBINDO O DATAFRAME
print(f"\n{df_vendedores}\n")

# CÁLCULOS
soma_janeiro = df_vendedores["Janeiro"].sum()
media_janeiro = df_vendedores["Janeiro"].mean()
maior_janeiro = df_vendedores["Janeiro"].max()
menor_janeiro = df_vendedores["Janeiro"].min()
vendedor_maior_janeiro = df_vendedores[df_vendedores["Janeiro"] == maior_janeiro]["Nome"]

print("          JANEIRO")
# RESULTADOS
print(f"TOTAL DE VENDAS: R${soma_janeiro}\nMÉDIA DE VENDAS: R${media_janeiro:.0f} \nMAIOR VENDA: R${maior_janeiro} \nMENOR VENDA: R${menor_janeiro}\n")
print(f"VENDEDOR COM MAIOR VENDA: {vendedor_maior_janeiro.values[0]}\n") # VALUES[0] para retornar somente os valores da coluna, sem a posição 
