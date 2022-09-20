#a
def numeros(L, i = 0, c = 0):
    if i == len(L) and c == 0:
        return True
    elif i < len(L):
        if type(L[i]) == int or type(L[i]) == float:
            return numeros(L, i + 1, c)
        else:
            return numeros(L, i + 1, c + 1)
    return False

def numeros2(L, i = 0):
    if len(L) == 0:
        return True
    elif i < len(L):
        if type(L[i]) == int or type(L[i]) == float:
            return numeros2(L[1:], i + 1)
        return False
    return True

L = [1, 2, 3, 4.4]
R = [1, 2, "3", 4]
print(numeros(L))
print(numeros(R))
print(numeros2(L))
print(numeros2(R))

#b
def media(L, i = 0, s = 0):
    if i == len(L):
        return s
    return media(L, i + 1, s + L[i])

X = [1, 2, 3, 2, 2]
print(media(X))

#c NÃO TEMINEI
def maiorMenor(L, i = 0, ma = 0, me = 0):
    if i == len(L):
        return ma, me
    else:
        if ma >= L[i] and ma >= me:
            return maiorMenor(L, i + 1, ma = L[i])
        elif me < L[i] and me < ma:
            return maiorMenor(L, i + 1, ma, me = L[i])
    return ma, me
print(X[:1])
print(maiorMenor(X))

#d NÃO TERMINEI
def reverso(L, i = 0, R = []):
    s = L[:1]
    if len(L) == 0:
        return R
    else:
        return reverso(L[1:], i + 1, s + R)

print(reverso(X))

#e
def contar(L, x, i = 0, c = 0):
    if i == len(L):
        return c
    else:
        if x == L[i]:
            return contar(L, x, i + 1, c + 1)
        else:
            return contar(L, x, i + 1, c)

print(contar(X, 2))

#f
def divisores(n, L = [], i = 1):
    if i > n:
        return L
    else:
        if n % i == 0:
            return divisores(n, L + [i], i + 1)
        else: 
            return divisores(n, L, i + 1)

print(divisores(6))


