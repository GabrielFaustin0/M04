import numpy as np

numeros=np.array([10,14,-5,33,120])

for i in range(5):
    print(numeros[i])
for i in range(5):
    numeros[i]=0
array_0d=np.array(40)
print(type(numeros))
print(type(array_0d))
print(array_0d)

print(numeros.ndim)

for i in range(5):
    print(numeros[i])

for x in numeros:
    print(x)

for x in range(len(numeros)):
    print(numeros[x])


vasio=np.empty(10)
print(vasio)

zeros= np.zeros(10)
print(zeros)