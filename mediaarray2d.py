import numpy as np
matriz=np.empty((10,5),dtype="i")
for a in range(matriz.shape[0]):
    for d in range(matriz.shape[1]):
        matriz[a,d]=input(f"intruduza a nota do aluno {a+1} e da dechiplina {d+1}")
melhormedia=0
for a in range(matriz.shape[0]):
    soma=0
    for d in range(matriz.shape[1]):
        soma=soma+matriz[a,d]
    media=soma/10
    if media>melhormedia:
        melhormedia=media

    print(f"o aluno {a+1} é {media}")
for d in range(matriz.shape[1]):
    soma=0
    for a in range(matriz.shape[0]):
        soma=soma+matriz[a,d]
    print(soma/5)