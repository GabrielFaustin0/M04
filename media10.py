import numpy as np
NR_alunos=10
notas = np.zeros(NR_alunos)
for n in range(NR_alunos):
    notas[n] =int(input(f"Nota do aluno nº{n+1}:"))
soma=0
for n in range(NR_alunos):
    soma=soma+notas[n]
media=soma/NR_alunos
print(f"A media das notas dos alunos é{media}")
for n in range(NR_alunos):
    if notas[n]>media:
        print(f"a nota {notas[n]} do aluno nº {n+1} é superior á media")