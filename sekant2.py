import math

def fx(x):
    return (math.e**x)/x-math.sin(x)/x**2+2*x-10

iter = 0
xn = 5
xneksibir = 10

while xneksibir != xn:
    iter+=1
    xnartibir = xn - fx(xn)*(xneksibir-xn)/(fx(xneksibir)-fx(xn))
    print(f"{iter} tekrarda bulunan x değeri: {xnartibir}")
    xneksibir = xn
    xn = xnartibir
    
