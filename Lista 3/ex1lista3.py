# a. NÃO TERMINEI
def palindromo(n):
    a = n // 1000
    b = n // 100 - a * 100
    c = n // 10 - a * 100 - b * 10
    d = n - n * 1000 - b * 100 - c * 10
    if 1000 <= n <= 9999:
        if a == d and b == c:
            print(n)
            return palindromo(n + 1)
        return palindromo(n + 1)
    elif n < 1000:
        return palindromo(n + 1)

# b.
def numero(n, i = 1):
    if i <= n:
        print(i)
        numero(n, i + 1)

# c.
def numeros(a, b):
    if a <= b:
        print(a)
        numeros(a + 1, b)

# d.
def potencia(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * potencia(a, b - 1)

print(potencia(2,0))
print(potencia(2,1))
print(potencia(2,2))
print(potencia(2,3))


# e. NÃO TERMINEI
def divisores(n, i = 1, c = 0):
    if i == n:
        return c + 1
    else:
        if n % i == 0:
            return divisores(n, i + 1, c + 1)
        else:
            return divisores(n, i + 1, c)    

# f.
def primo(n, i = 1, c = 0):
    if i == n:
        c + 1
        if c == 2:
            return True
        return False
    else:
        if n % i == 0:
            return divisores(n, i + 1, c + 1)
        else:
            return divisores(n, i + 1, c)  

# g.
def soma(n, r = 0, s = 0):
    if n < 10:
        s += n
        print(s)
    else:
        r = n % 10
        n = n // 10
        return soma(n, r, s + r)
