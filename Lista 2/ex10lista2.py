import math as m

def areaQuadrado(r):
    return m.pow(r,2)

def areaCirculo(r):
    return 2*m.pi*m.pow(r,2)

def areHexagono(r):
    return ((3*m.sqrt(3))/2)*m.pow(r,2)

def imprime(f):
    print(f"A área é {f:.1f}.")

print(imprime(2, areaQuadrado(2)))
print(imprime(2, areaCirculo(2)))
print(imprime(2, areHexagono(2)))
