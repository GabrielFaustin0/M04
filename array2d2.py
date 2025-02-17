import numpy as np
matriz=np.zeros((5,3),dtype="i")
for l in range(matriz.shape[0]):
    for c in range(matriz.shape[1]):
        matriz[l,c]=l*c
print(matriz)