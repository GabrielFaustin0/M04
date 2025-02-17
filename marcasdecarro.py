import numpy as np
marcas=np.array(["Tesla","Volvo","BMW","Peugeot","Tesla","Mercedes","Ford"])
marcas_aparcidas=np.zeros(10,"U15")
n=0
for i in marcas:
    if i in marcas_aparcidas:
        continue
    marcas_aparcidas[n]=i
    n=n+1
    n_marcas=0
    for k in marcas:
        if i==k:
            n_marcas=n_marcas+1
    print(f"isistem {n_marcas} carros da marca {i}")

