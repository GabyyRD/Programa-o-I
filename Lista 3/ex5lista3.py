import math

def potencia(x, n):
    if n == 0:
        print(0)
    elif n % 2 == 0:
        print(pow(pow(x, (n/2)), 2))
    else:
        print(pow(pow(x, ((n-1)/2)), 2) * x)

potencia(2, 3)
