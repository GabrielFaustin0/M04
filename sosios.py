import numpy as np
nsociosA=int(input("quantos socios a no clube A"))
nsociosB=int(input("quantos socios a no clube B"))
sociosA=np.empty(nsociosA,dtype="U15")
sociosB=np.empty(nsociosB,dtype="U15")
sociosc=np.empty(nsociosA, dtype="U15")
contar=0
for i in range(nsociosA):
    sociosA[i]=input("socioA:")
for i in range(nsociosB):
    sociosB[i]=input("socioB:")
for i in sociosA:
    for k in sociosB:
        if sociosA[i]==sociosB[k]:
            sociosc[i]=sociosA[i]
print(sociosc)
