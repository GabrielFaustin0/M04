import numpy as np
dinerom=np.array([[0.01,10],[0.02,5],[0.05,6],[0.10,2],[0.50,10],[1,1],[2,1]])
valor_apagar=float(input())
valor_entregue=float(input())
troco=valor_entregue-valor_apagar
if troco==0:
    print("volte sempre")
else:
    for m in range(len(dinerom)-1,-1,-1):
        if dinerom[m]<troco and stock[m]>0:
            moedas_adevolver=moedas_adevolver+str(moedas[m])+","
            troco=troco-moeda[m]
            stock[m]=stock[m]-1
        p