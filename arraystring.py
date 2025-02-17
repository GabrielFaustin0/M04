import numpy as np

"""
i=inteiros
f=reais
b=boleano
s=strings
u=unicode
m=datetime
"""
nomes = np.empty(10,dtype="U20")
for i in range (len(nomes)):
    nomes[i]= input("intruduza o nome")
print(nomes)