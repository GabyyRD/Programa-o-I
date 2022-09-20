import math as m
# 1)
# a.
def maximo(x,y):
    return x if x > y else y

# b.
def absoluto(n):
    return n if n >= 0 else -n

# c.
def divisivel(d):
    return True if d//5==0 else False


# d.
def crescente(a, b, c):
    if a >= b and b >= c:
        print(a, b, c)
    elif a >= b and c >= b:
        print(a, c, b)
    elif b >= a and a >= c:
        print(b, a, c)
    elif b >= a and c >= a:
        print(b, c, a)
    elif c >= a and a >= b:
        print(c, a, b)
    elif c >= a and b >= a:
        print(c, b, a)

# e.
def crescente(a, b, c):
    if a >= b and b >= c:
        return a, b, c
    elif a >= b and c >= b:
        return a, c, b
    elif b >= a and a >= c:
        return b, a, c
    elif b >= a and c >= a:
        return b, c, a
    elif c >= a and a >= b:
        return c, a, b
    elif c >= a and b >= a:
        return c, b, a

# f.
def esfera(r):
    area = 4*m.pi*m.pow(r,2)
    volume = (4/3)*m.pi*m.pow(r,3)
    return print(f"{area}\n {volume}")

# g.
def soma(a, b, c):
    if a >= b >= c or b >= a >= c:
        return m.pow(a,2)*m.pow(b,2)
    elif a >= c >= b or c >= a >= b:
        return m.pow(a,2)*m.pow(c,2)
    elif b >= c >= a or c >= b >= a:
        return m.pow(b,2)*m.pow(c,2)

# h.
def converteTempo(s):
    h = s//3600
    m = (s%3600)//60
    s = (s%3600)%60
    print(f"{h:02}:{m:02}:{s:02}")

# i.
def somaMedia(a, b, c, d, e):
    somaPar = 0
    somaImpar = 0
    contaPar = 0
    if a % 2 == 0:
        somaPar + a
        contaPar += 1
    else: somaImpar + 1
    if b % 2 == 0:
        somaPar + b
        contaPar += 1
    else: somaImpar + 1
    if c % 2 == 0:
        somaPar + c
        contaPar += 1
    else: somaImpar + 1
    if d % 2 == 0:
        somaPar + d
        contaPar += 1
    else: somaImpar + 1
    if e % 2 == 0:
        somaPar + e
        contaPar += 1
    else: somaImpar + 1
    mediaPar = somaPar/contaPar

    if contaPar < 5:
        mediaImpar = somaImpar/(5-contaPar)
    else:
        mediaImpar == 0
    print(somaPar, somaImpar, mediaPar, mediaImpar)

# j.
def tipo(t):
    print(type(t))

# k.
def ascendente(n):
    p = n//100
    s = (n//10)-(p*10)
    t = n - p*100 - s*10
    print(p,s,t)
    if type(n)==int and 100 <= n <= 999:
        if p > s > t:
            return True
        return False
    return False

# l.  
def palindromo(n):
    p = n // 1000
    s = n // 100 - p*10
    t = n // 10 - p*1000 - s*100
    q = n - p*1000 - s*100 - t*10
    if type(n) == int and 1000 <= n <= 9999:
        if p == q and s == t:
            return True
        return False
    return False
