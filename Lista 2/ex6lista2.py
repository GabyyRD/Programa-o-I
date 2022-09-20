def verifica(n):
    p1 = n // 100
    p2 = n % 100
    d = p1 + p2
    if 1000 <= n <= 9999:
        if d**2 == n:
            return True
        return False
    return False

def main():
    n = int(input())
    if verifica(n) == True:
        print(f"{n} possui a propriedade.")
    else:
        print(f"{n} não possui a propriedade.")

main()