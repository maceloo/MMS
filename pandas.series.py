# USANDO SSERIES
import pandas as pd
media = pd.Series([80,90,100,10,20,70,50,65,15,95])
ap = media[media >= 70]
rp = media[media < 70]
print(f"--- Notas maiores que 70 --- ") 
print(ap)
print("\n--- Notas menores que 70 --- ")
print(rp)