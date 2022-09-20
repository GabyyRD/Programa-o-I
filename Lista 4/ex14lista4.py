#Compreensão de listas

lista1 = [x**2 + 2 for x in range(11)]
lista2 = [x for x in range(-100, 101) if x % 3 == 0 and x % 5 == 0]
#lista3 = [x for x in range(0, 501)] #numero perfeito

def divisores(numero, i = 1, d = 0):
    if i > numero:
        return d
    elif numero % i == 0:
        return divisores(numero, i + 1, d + 1)
    return divisores(numero, i + 1, d)

lista4 = [x for x in range(0, 101) if divisores(x) == 2]
#lista5 = [fibonacci(x) for x in range(1, 11)]

print(lista1)
print(lista2)
print(lista4)