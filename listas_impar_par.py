# IMPAR - PAR
par = 0
impar = 0
num = [1,12,14,37,55,91,88,4,41,17]
for i in range(len(num)):
    if num[i] % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"A quantidade de números pares é: {par}")
print(f"A quantidade de números ímpares é: {impar}")
print("         ---ORDEM DE CRIAÇÃO---")
print(num)
print("         ---ORDEM REVERSA---")
num.reverse()
print(num)
print("         ---ORDEM CRESCENTE---")
num.sort()
print(num)