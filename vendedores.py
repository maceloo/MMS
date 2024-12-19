# RELATÓRIO VENDEDORES

import pandas as pd
def formatar(valor):
    return "{:.2f}%".format(valor)

maria = pd.Series([800,700,1000,900,1200,600,600])
joao = pd.Series([900,500,1100,1000,900,500,700])
manuel = pd.Series([700,600,900,1200,900,700,400])

maria_total = maria.sum()
maria_media = maria.mean()
maria_maior = maria.max()
maria_menor = maria.min()
print("\n      MARIA")
print(f"TOTAL DE VENDAS: {maria_total} \nMÉDIA DE VENDAS: {maria_media:.0f} \nMAIORES VENDAS: {maria_maior} \nMENORES VENDAS: {maria_menor}" )

joao_total = joao.sum()
joao_media = joao.mean()
joao_maior = joao.max()
joao_menor = joao.min()
print("\n      JOÃO")
print(f"TOTAL DE VENDAS: {joao_total} \nMÉDIA DE VENDAS: {joao_media:.0f} \nMAIORES VENDAS: {joao_maior} \nMENORES VENDAS: {joao_menor}" )

manuel_total = manuel.sum()
manuel_media = manuel.mean()
manuel_maior = manuel.max()
manuel_menor = manuel.min()
print("\n      MANUEL")
print(f"TOTAL DE VENDAS: {manuel_total} \nMÉDIA DE VENDAS: {manuel_media:.0f} \nMAIORES VENDAS: {manuel_maior} \nMENORES VENDAS: {manuel_menor} \n" )
