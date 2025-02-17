import numpy as np
temperaturas = np.empty(12,dtype="i")
soma=0
for i in range(1,12):
    temperaturas[i]=int(input(f"A tempera do mês{i}"))
    soma=temperaturas[i]+soma
media=soma/12
print(round,media,2)
maior=temperaturas[0]
menor=temperaturas[0]
for i in range(1,12):
    if temperaturas[i]>maior:
        maior=temperaturas[i]
    if temperaturas[i]<menor:
        menor=temperaturas[i]
                           
print(f"maior temperatura {maior} mrnor {menor}")
nmoda=0
for i in range(1,12):
    contar=0
    for k in range(1,12):
        if temperaturas[i]==temperaturas[k]:
            contar=contar+1
    if contar>nmoda:
        nmoda=contar
        moda=i
print(f"a moda é a temperatura{temperaturas[moda]} que ocurreu {nmoda}")


