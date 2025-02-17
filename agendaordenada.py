import numpy as np
nr_max=10
def main():
    op=1
    contactos=np.zeros(nr_max,"U30")
    while op!=4:
        op=int(input("1.adicionar\n2.listar\n3.pesquisar\n4.Terminar"))
        if op==1:
             nome=input("nome do contacto a adicionar:")
             data=input("data de nachimento")
             adicionar(contactos,nome+"-"+data)
        elif op==2:
            listar(contactos,nome)
        elif op==3:
            pesquisar(contactos,nome)
def adicionar(contactos,nome):
    if contactos[0]=="":
        contactos[0]=nome
        return
    if contactos[nr_max-1]:
        print("a agenda esta cheia")
        return
    for posição in range(nr_max):
        if nome<contactos[posição]:
            break
    for i in range(nr_max):
        contactos[i]=contactos[i-1]
    contactos[posição]=nome
def listar(contactos,nome):
    for nome in contactos:
        if nome!="":
            partes=nome.split("-")
            print(f"nome: {partes[0]} Data de nachimento: {partes[1]}")
def pesquisar(contactos,nome):
    primeiro=0
    ultimo=len(contactos)-1
    for t in contactos:
        if t=="":
            break
        ultimo=ultimo+1
    while primeiro<=ultimo:
        meio=(primeiro+ultimo)//2
        valor_meio=contactos[meio]
        if nome in valor_meio:
            print(valor_meio)
            return
        elif valor_meio<nome:
            primeiro=meio+1
        else:
            ultimo=meio-1
    print("O valor não exeste")
main()