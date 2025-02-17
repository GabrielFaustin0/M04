nome1=input("digite o seu nome completo")
nome2=input("digite o seu nome completo")
nome1=nome1.split(" ")
nome1=(nome1[-1::])
nome2=nome2.split(" ")
nome2=(nome2[-1::])
if nome1==nome2:
    print("são da mesma familia")
else:
    print("não são da mesma familia")