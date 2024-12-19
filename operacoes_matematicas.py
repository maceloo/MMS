# FAZENDO OPERAÇÕES MATEMÁTICAS EM SERIES
import pandas as pd
num_1 = pd.Series([10,20,30,40,50])
num_2 = pd.Series([10,20,30,40,50])
soma = num_1 + num_2
print(f"A SOMA entre os números é:\n{soma}")
sub = num_1 - num_2
print(f"A SUBTRAÇÃO ente os números é:\n{sub}")
multi = num_1 * num_2
print(f"A MULTIPLICAÇÃO entre os números é:\n{multi}")
divi = num_1 / num_2
print(f"A DIVISÃO entre os números é:\n{divi}")
