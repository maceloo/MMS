# VELOCIDADE MEDIA
desloc = int(input("Qual foi o deslocamento total da viagem? "))
tempo = int(input("Qual foi o tempo total da viagem? "))
velo_media = int(desloc / tempo)
ms = int(velo_media / 3.6)
print(f"A velocidade média em sua viagem foi de {velo_media:.2f}Km/H, o mesmo que {ms:.2f}m/s")

# CONSUMO MÉDIO
litros = int(desloc/12)
conusmo_medio = int(desloc / litros)
print(f"Foi gasto nessa viagem {litros}L de combustível, significa que o veículo fez um consumo médio de  {conusmo_medio:.2f}Km/L")
