import math
numero = float(input())
raiz = math.sqrt(numero)
loge = math.log(numero)
log10 = math.log10(numero)
pot = pow(numero, 2)
e = math.exp(1)
log2 = math.log2(numero)
pot2 = pow(numero, numero/2)
if numero <= 1:
    print(loge)
elif 1 < numero <=2:
    print(f"{log10 + raiz}")
elif 2 < numero <= 5:
    print(f"{pot + e}")
elif numero > 5:
    print(f"{pot2 + log2}")