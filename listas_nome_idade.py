# ARMAZENANDO E EXIBINDO DADOS DO VETOR 
nomes = []
idades = []
for i in range(2):
    nomes.append(input("Qual seu nome? ")) # APPEND é o comando para armazenar dados para um vetor/lista 
    idades.append(int(input("Informe a idade: ")))
print("LISTAGEM DOS USUÁRIOS:")
n = 1 # MÁSCARA 
for i in range(len(nomes)):
    print(f"{n}º - {nomes[i]} - {idades[i]} anos")
    n +=1