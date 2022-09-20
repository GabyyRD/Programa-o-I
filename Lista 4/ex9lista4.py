def buscaBinaria(L, x): 
    """ Função utilizada apenas para facilitar a chamada da função buscaBinariaR """
    return buscaBinariaR(L, x, 0, len(L)-1)

def buscaBinariaR(L, x, ini, fim):
    if len(L)%2 != 0 and x == L[int(len(L)/2)]:
        print(L)
        print(x)
    elif len(L) == 0:
        print(L)
        return
    elif x < L[int(len(L)/2)]:
        print(L)
        L = L[:L[int(len(L)/2)]]
        return buscaBinariaR(L, x, ini, fim)
    elif x > L[int(len(L)/2)]:
        print(L)
        L = L[L[(int(len(L)/2)-1)]:]
        return buscaBinariaR(L, x, ini, fim)
    else:
        print(L)
        return 

def main():
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    x = int(input("Número: "))
    buscaBinaria(L, x)

main()
