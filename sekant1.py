import math

def fx(x):
    return x*math.cos(x)-math.log(x)

iter = 0
xn = 2
xneksibir = 1
epsilon = 1

while epsilon > 10**-5:
    iter+=1
    xnartibir = xn - fx(xn)*(xneksibir-xn)/(fx(xneksibir)-fx(xn))
    print(f"{iter} tekrarda bulunan x değeri: {xnartibir}")
    xneksibir = xn
    xn = xnartibir
    epsilon = fx(xnartibir) 

    
