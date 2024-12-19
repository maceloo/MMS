# USANDO LISTAS
media = [80,90,100,10,20,70,50,65,15,95]
ap = []
rp = []
for i in range(len(media)): 
    if media [i] >= 70:
        ap.append(media[i])
    else:
        rp.append(media[i])
print(f"--- Notas maiores que 70 --- ") 
print(ap)
print("\n--- Notas menores que 70 --- ")
print(rp)
        