import math

def fx(x):
    return math.e**(-1*x)-x

xn = 1
xneksibir = 0
iter = 0

while xneksibir != xn:
    iter+=1
    xnartibir = xn - fx(xn)*(xneksibir-xn)/(fx(xneksibir)-fx(xn))
    print(f"{iter} tekrarda bulunan x değeri: {xnartibir}")
    xneksibir = xn
    xn = xnartibir
    
