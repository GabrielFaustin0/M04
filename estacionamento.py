import numpy as np
todas_matriculas=np.zeros(10)
tempo=np.zeros(10)
matriculas=input("escreva todas as matriculas separadas por virgulas")
matriculas =matriculas.split(",")
segundos=input("degite quanto tempo em segundos separado por cirgulas")
segundos =segundos.split(",")
if len(matriculas)!=len(segundos):
    print("O nº  tem de ser igual")
if len (matriculas)>10:
    print("meteu demasiadas matriculas")
for i in range(len(matriculas)):
    todas_matriculas=matriculas[i].strip()
    tempo[i]=int(segundos[i].strip())
def media():
    tempo_maior=0
    for i in range(10):
        if tempo[i]>tempo_maior:
            tempo_maior=i
    print(todas_matriculas[tempo_maior])
    for i in range (10):
        soma=+tempo[i]
    media=soma/len(tempo)
    return media
def supamedia():
    media=media()

    
def carro2(todas_matriculas):
    for i in todas_matriculas:
        contar=1
        for k in todas_matriculas:
            if i ==k:
                contar=contar+1
    if contar>1:
        print(f"a matricula{i}esteve estacionada{contar}veses.")

    
