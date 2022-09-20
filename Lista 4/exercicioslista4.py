#Número 2
def confere(N, i = 1, c = 0):
    if i <= N:
        if N % i == 0:
            return confere(N, i + 1, c + 1)
        return confere(N, i + 1, c)
    else:
        if c == 2:
            return True
    return False

def primo(n, L = [], i = 2, c = 0):
    if c == n:
        return L
    else:
        if confere(i) == True:
            return primo(n, L + [i], i + 1, c + 1)
        return primo(n, L, i + 1, c)

print(primo(5))

#Número 3
def listaNova(l1, l2, L = [], i = 0, R = []):
    R = l1 + l2
    if i < len(R):
        if R[i] in L:
            return listaNova(l1, l2, L, i + 1, R)
        else:
            return listaNova(l1, l2, L + [R[i]], i + 1, R)
    return L

#Número 4
def semRepetidos(l1, L = [], i = 0):
    if i < len(l1):
        if l1[i] in L:
            return semRepetidos(l1, L, i + 1)
        else:
            return semRepetidos(l1, L + [l1[i]], i + 1)
    return L

l1 = [1, 2, 3, 3]
l2 = [1, 5, 3]
print(semRepetidos(l1))
print(listaNova(l1, l2))

#Número 5
def intersecao(l1, l2, L = [], i = 0):
    if i < len(l1):
        if l1[i] in l2 and l1[i] not in L:
            return intersecao(l1, l2, L + [l1[i]], i + 1)
        else:
            return intersecao(l1, l2, L, i + 1)
    return L

print(intersecao(l1, l2))

#Número 6
def crescente(l, i = 0):
    if i < len(l) - 1:
        if l[i] <= l[i + 1]:
            return crescente(l, i + 1)
        return False
    return True

l3 = [1, 3, 5, 6]
l4 = [1, 4, 3, 9, 7]
print(crescente(l1))
print(crescente(l3))
print(crescente(l4))

#Número 7
def numeros(L = []):
    n = int(input())
    if n < 0 or n > 9:
        return resultado(L)
    else:
        return numeros(L + [n])

def resultado(L, i = 0, p = 0, c = 0):
    if i <= 9:
        if p < len(L):
            if i == L[p]:
                return resultado(L, i, p + 1, c + 1)
            else:
                return resultado(L, i, p + 1, c)
        else:
            print(f"{i}: {c}")
        return resultado(L, i + 1, p = 0, c = 0)
