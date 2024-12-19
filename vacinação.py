# VACINAÇÃO NA POPULAÇÃO

import pandas as pd
def formatar(valor): #função para formatar 
    return "{:.2f}%".format(valor)
    
# banco de dados
populacao_vacinada = pd.Series([30000000, 25000000, 10000000, 5000000])
populacao_total = pd.Series([213317639, 214477744, 215574303, 216687971])

total_vacinado = populacao_vacinada.sum()
media_vacinado = populacao_vacinada.mean()
print("\n         VACINAÇÃO")
print(f"TOTAL DE PESSOAS VACINADAS: {total_vacinado} PESSOAS!")
print(f"MÉDIA DE PESSOAS VACINADAS: {media_vacinado} PESSOAS! ")

total_populacao = populacao_total.sum()
media_populacao = populacao_total.mean()
print("\n         POPULAÇÃO")
print(f"TOTAL DA POPULAÇÃO: {total_populacao} PESSOAS!")
print(f"MEDIA DE PESSOAS: {media_populacao} PESSOAS")

print("\n         TAXA DE VACINAÇÃO ANUAL")
taxa_vac = (total_vacinado / populacao_total)
tv = (taxa_vac * 100).apply(formatar)
print(tv)

tot_tx_vac = (populacao_vacinada.sum() / populacao_total.sum()) * 100
print(f"\nPERCENTUAL DE PESSOAS VACINADAS NO PERÍODO: {tot_tx_vac:.2f}% \n")
