import math 

def fx(x):
    return x**3-x-1

def fx_der(x):
    return 3*x**2-1

kok = 1.5
eps = 1
iterasyon = 0
while eps > 10 ** -5:
    iterasyon+=1
    yenikok = kok - fx(kok)/fx_der(kok)
    eps = abs(fx(kok)/fx_der(kok))
    print(f"{iterasyon} tekrarda bulunan x değeri: {yenikok}, epsilon değeri: {eps:.20f}")
    kok = yenikok
