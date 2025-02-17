nome=input("digite o seu nome completo")
name=nome.split(" ")
if len(name)==1:
    print(nome)
ultimonome=name[len(name)-1]+", "
for i in name[:len(name)-1]:
    ultimonome=ultimonome+i+" "
print(ultimonome.strip())