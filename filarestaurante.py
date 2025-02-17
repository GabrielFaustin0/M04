import numpy as np
nrmax=10

def main():
    fila=np.empty(nrmax,dtype="U15")
    for i in range(nrmax):
        fila[i]=""
    op=1
    while op!=4:
        op=int(input("1.Entrada\n2.Saída\n3.Consultar a Fila\n4.Terminar"))
        if op==1:
            entrada(fila)
        elif op==2:
            saida(fila)
        elif op==3:
            consultar(fila)

def entrada(fila):
    encontrou=False
    for posicao in range(nrmax):
        if fila[posicao]=="":
            encontrou=True
            break
    if encontrou==False:
        print("Fila cheia. volte mais tarde")
        return
    nome=input("indique o nome para a fila de espera")
    fila[posicao]=nome
    print(f"a posição na fila de espera é {posicao+1}º")
        
def saida(fila):
    if fila[0]=="":
        print("não tem ninguem na fila de espera.")
        return
    print(f"o cliênte com o nome {fila[0]} pode entrar.")
    for i in range(nrmax-1):
        fila[i]=fila[i+1]
    fila[nrmax-1]=""
def consultar(fila):
    fila_cheia=True
    for i in range(nrmax):
        if fila[i]=="":
            fila_cheia=False
            break
        print(f"{i+1}º - {fila[i]}")
    if fila_cheia==True:
        print("A fila está cheia")
main()