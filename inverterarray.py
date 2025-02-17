import numpy as np
nomes = np.empty(5,dtype="U15")
for i in range(5):
    nomes[i]=input("Digite um nome")
nomesinv=np.empty(5,dtype="U15")
k=4
for i in range(5):
    nomesinv[i]=nomes[k]
    k=k-1
print(nomesinv)