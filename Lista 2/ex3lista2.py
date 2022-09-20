import math as m

def calculo():
    x = int(input())
    if x <= 1:
        return m.log(abs(x))
    elif x <= 2:
        return m.log10(x) + m.sqrt(x)
    elif x <= 5:
        return m.pow(x,2) + m.exp(x)
    elif x > 5:
        return m.pow(x,(x/2)) + m.log2(x)

calculo()
