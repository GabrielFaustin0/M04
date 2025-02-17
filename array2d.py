"array 2d"
import numpy as np
matriz=np.array([[1,2,3],[3,5,0]])
print (matriz)
print(matriz[0,0])
print(matriz[1,2])
for l in range(2):
    for c in range(3):
        print(matriz[l,c])
