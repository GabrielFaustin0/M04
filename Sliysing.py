import numpy as np
"""
slicing - permite ter acesso a um subconjunto de uma sequência ou coleção
    Sintaxe : sequencia [inicio:fim:passo]
    Inicio  - a posição do prinmeiro a incluir
    fim     - é posição onde termina o slice Não é incluido
    passo   - intervalo entre os elmentos a incluir no slice
"""
print("#"*100)
nome="Joaquim Silva"
nome_5_letras=nome[0:5:1]
print(nome_5_letras)
nome_5_letras=nome[:5:1]
print(nome_5_letras)
nome_5_letras=nome[8:]
print(nome_5_letras)
nome_invertido=nome[::-1]
print(nome_invertido)
nome_5_letras=nome[::2]
print(nome_5_letras)
print(nome[-1])
print(nome[:7:-1])
print("#"*100)

nomes=np.array(["Joaquim","maria","antónio","augosto","cézar"])
#mostrar todos os nomes por ordem imvertida
print(nomes[::-1])
#mostrar os dois ultimos nomes
print(nomes[3::])
#mostrar o 1º,3º,5º
print(nomes[::2])
#---------------------------------------------------------------
print(nomes[0][::-1])
print("#"*100)