def ehPerfeito(n, i = 1, s = 0):
    if type(n) != int:
        return False
    elif n == i:
        if n == s:
            return True
        return False
    elif n % i == 0:
        return ehPerfeito(n, i + 1, s + i)
    return ehPerfeito(n, i + 1, s)

def contaNumPerfeitos(n, i = 1, c = 0):
    if type(n) == int:
        if i <= n:
            if ehPerfeito(i) == True:
                print(i)
                return contaNumPerfeitos(n, i + 1, c + 1)
            return contaNumPerfeitos(n, i + 1, c)
    return

def main():
    x = int(input())
    contaNumPerfeitos(x)

main()