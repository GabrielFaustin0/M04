import numpy as np
proibidas=np.array(["mau","Pobre","infeliz","péssimo"])
alternativas=np.array(["bom","rico","feliz","ótimo"])
frase=input("digite uma frase")
for i in range(len(proibidas)):
    if proibidas[i] in frase:
        frase=frase.replace(proibidas[i],alternativas[i])
print(frase)