def myFilter(funcao, lista, i = 0, novaLista = []):
    if i == len(lista):
        return novaLista
    elif funcao(lista[i]):
        novaLista += [lista[i]]
    return myFilter(funcao, lista, i + 1, novaLista)

#Exemplo:
l1 = list(range(2, 101))

#a. Números divisíveis por 3 e 5:
print(myFilter(lambda x : x % 3 == 0 and x % 5 == 0, l1))

#b. Números primos.:
def divisores(numero, i = 1, d = 0):
    if i > numero:
        return d
    elif numero % i == 0:
        return divisores(numero, i + 1, d + 1)
    return divisores(numero, i + 1, d)

print(myFilter(lambda x : divisores(x) == 2, l1, i = 0, novaLista = []))