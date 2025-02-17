nome1=input("digite o seu nome completo")
nome2=input("digite o seu nome completo")
nome1=nome1.split(" ")
nome2=nome2.split(" ")
for i in nome1[1::]:
    for k in nome2[1::]:
        if i==k:
            print("São da mesma familia")
            break
        else:
            print("não sao da mesma familia")