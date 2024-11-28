# USO DE LISTAS
nome_01 = "Marcelo, Hugo, Lucas" #STR
nome_02 = ["Marcelo", "Hugo", "Lucas"]
print(nome_01)
print(nome_02)
print(nome_02[0])
print(len(nome_02)) #LEN É O COMANDO PARA LER A QUANTIDADE DOS VETORES
print("LISTAGEM DOS ELEMENTOS DO VETOR:")
n = 1
for i in range(len(nome_02)):
    print(f"{n}º - {nome_02[i]}")
    n += 1 #MÁSCARA PARA FAZER LISTAGEM
