import numpy as np
Limitemaxagenda=100
nomes = np.empty(Limitemaxagenda,dtype="U50")
numero=np.empty(Limitemaxagenda,dtype="i")
email=np.empty(Limitemaxagenda,dtype="U50")
n_contatos=0
def menu():
    op="1"
    while op!=6:
        print("1. Adicionar\n2. Listar Todos\n3. Procurar\n4. Apagar\n5. editar\n6. Terminar")
        op=int(input(""))
        if op==1:
            adicionar(nomes,numero,email)
        elif op==2:
            listartodos(nomes,numero,email)
        elif op==3:
            procurar(nomes,numero,email)
        elif op==4:
            apagar(nomes,numero,email)
        elif op==5:
            editar(nomes,numero,email)

def adicionar(nomes,numero,email):
    global n_contatos 
    nomes[n_contatos]=input("digite o nome")
    numero[n_contatos]=int(input("digite o numero"))
    email[n_contatos]=input("digite o email")
    n_contatos=n_contatos+1

def listartodos(nomes,numero,email):
    global n_contatos
    for i in range (n_contatos):
        print(nomes[i])
        print(numero[i])
        print(email[i])
def procurar(nomes,numero,email):
    global n_contactos
    nome=input("Procurar:")
    for i in range(n_contatos):
        if nomes[i]==nome:
            print(nomes[i])
            print(numero[i])
            print(email[i])

def apagar(nomes,numero,email):
    global n_contatos
    nome=input("esclui:")
    for i in range(n_contatos):
        if nome in nomes[i]:
            print(nomes[i])
            print(numero[i])
            print(email[i])
            op=input("tem assertesa que quer apagar  S\N")
            if op in "ss":
                for k in range(i,n_contatos):
                    if k == max:
                        nomes[k]=nomes[k+1]
                        email[k]=email[k+1]
                        numero[k]=numero[k+1]
                        n_contatos=n_contatos-1
def editar(nomes,numero,email):
    nome=input("Qual o nome do cotacto a edita")
    for i in nomes[i]:
        print(f"Dados do contacto:{nomes[i]}-{numero[i]}-{email[i]}")
        op=input("prentende editar estes dados? (S,N) ")
        if op.lower()!="s":
            continue
        novonome=input("intrudusa o novo nome ou deche em branco para nao alterar")
        novonumero=int(input("intrudusa o novo numero ou deche em branco para nao alterar"))
        novoemail=input("intrudusa o novo email ou deche em branco para nao alterar")
        


        
menu()