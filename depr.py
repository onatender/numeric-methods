def fx(x):
    return x**3-7*x**2+14*x-6

def fx_der(x):
    return 3*x**2-14*x+14

kok = 0
eps = 1
iterasyon = 0

while eps > 10 ** -6:
    iterasyon+=1
    yenikok = kok - fx(kok)/fx_der(kok)
    eps = abs((yenikok - kok)/yenikok)
    print(f"{iterasyon} tekrarda bulunan x değeri: {yenikok}, epsilon değeri: {eps:.20f}")
    kok = yenikok
