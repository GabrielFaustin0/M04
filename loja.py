import numpy as np
MaxClientes=10
cliêntes = np.empty(MaxClientes,dtype="U50")
compras=np.empty(MaxClientes,dtype="f")
def lerdados(cliêntes,compras):
    nclientes=int(input("quantos clientes entraram na loja"))
    for i in range(nclientes):
        cliêntes[i]=input("Nome:")
        compras[i]=input("Valor das compras")
def quemmais(cliêntes,compras):
    #maiorcompra=compras[0]
    posição=0
    for i in range(MaxClientes):
        if compras[posição]<compras[i]:
            posição=i
    print(f"O melhor cliente foi {cliêntes[posição]} que gastou{compras[posição]}")
lerdados(cliêntes,compras)
quemmais(cliêntes,compras)