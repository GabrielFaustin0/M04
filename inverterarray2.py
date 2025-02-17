import numpy as np
nomes = np.empty(5,dtype="U15")
for i in range(5):
    nomes[i]=input("Digite um nome")
k=4
for i in range(5//2):
    temp=nomes[i]
    nomes[i]=nomes[k]
    nomes[k]=tempk=k-1
print(nomes)