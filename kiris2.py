import math

def fx(x):
    return x*math.e**x-2

xsifir = 0.85
xn = 0.9
epsilon = 1

iter = 0
while epsilon > 0.008:
    iter+=1
    xnartibir = xsifir-((xn-xsifir)/(fx(xn)-fx(xsifir)))*fx(xsifir)
    print(f"{iter} tekrarda bulunan x değeri: {xnartibir}, epsilon değeri: {abs(xnartibir-xn):.20f}")
    epsilon = abs(xnartibir-xn)
    xn = xnartibir