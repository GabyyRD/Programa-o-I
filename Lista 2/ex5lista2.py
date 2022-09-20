from math import sqrt

def delta(a, b, c):
    d = b**2 - 4*a*c
    return d

def raizes(a, b, d):
    raizDelta = sqrt(d)
    if d < 0:
        print("A equação não possui raízes reais.")
    elif d == 0:
        x = b/(2*a)
        print(f"A raiz da equação é {x}.")
    elif d > 0:
        x1 = (b + raizDelta)/(2*a)
        x2 = (b - raizDelta)/(2*a)
        print(f"As raízes da equação são {x1} e {x2}.")

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    delta(a, b, c)
    raizes(a, b, delta(a, b, c))

main()
