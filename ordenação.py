"""
Emplementar a ordençao bubble sort com um array
"""
import numpy as np
numeros=np.array([500,3,379,140,104])
def bubble_sort(vetor):
    tamanho=len(vetor)
    for i in range(tamanho):
        for j in range (0,tamanho-i-1):
            if vetor[j]>vetor[j+1]:
                t=vetor[j]
                vetor[j]=vetor[j+1]
                vetor[j+1]=t


print(numeros)
bubble_sort(numeros)
print(numeros)