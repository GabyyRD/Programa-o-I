import math

def myMap(funcao, lista, i = 0, novaLista = []):
    if i == len(lista):
        return novaLista
    else:
        novaLista += [funcao(lista[i])]
        return myMap(funcao, lista, i + 1, novaLista)


#Exemplo:
L = [2, 3, 4, 5]
print(myMap(math.sqrt, L))
