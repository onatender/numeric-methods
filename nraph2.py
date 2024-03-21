def fx(x):
    return x**3-2*x**2-5

def fx_der(x):
    return 3*x**2-4*x

kok = 2
eps = 1
iterasyon = 0
p = 2.69064744802878
while eps > 10 ** -4:
    iterasyon+=1
    yenikok = kok - fx(kok)/fx_der(kok)
    eps = abs(yenikok-p)
    print(f"{iterasyon} tekrarda bulunan x değeri: {yenikok}, epsilon değeri: {eps:.20f}")
    kok = yenikok
