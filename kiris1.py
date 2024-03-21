def fx(x):
    return x**3-20*x+16

xsifir = 3
xn = 5
epsilon = 1

iter = 0
while epsilon > 0.008:
    iter+=1
    xnartibir = xsifir-((xn-xsifir)/(fx(xn)-fx(xsifir)))*fx(xsifir)
    print(f"{iter} tekrarda bulunan x değeri: {xnartibir}, epsilon değeri: {abs(xnartibir-xn):.20f}")
    epsilon = abs(xnartibir-xn)
    xn = xnartibir