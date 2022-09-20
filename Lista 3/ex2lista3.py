def f(n):
    if isinstance(n, int) and n >= 0:
        if n > 2:
            return f(n-1) + f(n-2)
        return 1

def imprimef(n, i = 1):
    if isinstance(n, int) and n >= 0:
        if i <= n:
            print(f(i))
            imprimef(n, i + 1)
    else:
        print("Erro")
        return None

imprimef(10)
