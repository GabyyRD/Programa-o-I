def numeroPascal(n, k):
    if n == k or k == 0:
        return 1
    elif n != 1 and k == 1:
        return n
    else:
        return numeroPascal(n-1, k-1) + numeroPascal(n-1, k)


def trianguloPascal(linhas, linhaAtual = 1, n = 0, k = 0, quant = 1):
    if linhaAtual <= linhas:
        if quant == linhaAtual:
            print(numeroPascal(n, k))
        else:
            print(numeroPascal(n, k), end=" ")
            return trianguloPascal(linhas, linhaAtual, n, k + 1, quant + 1)
        return trianguloPascal(linhas, linhaAtual + 1, n = linhaAtual, k = 0, quant = 1)

def trianguloPascal2(linhas, linhaAtual = 1, n = 0, k = 0, quant = 1):
    if linhaAtual <= linhas:
        if linhaAtual <= 5:
            if quant == linhaAtual:
                print(numeroPascal(n, k))
            elif k == 0:
                print(" "*(linhas-linhaAtual), numeroPascal(n, k), end="   ")
                return trianguloPascal2(linhas, linhaAtual, n, k + 1, quant + 1)
            else:
                print(numeroPascal(n, k), end="   ")
                return trianguloPascal2(linhas, linhaAtual, n, k + 1, quant + 1)
        elif 6 <= linhaAtual <= 9: 
            if quant == linhaAtual:
                print(numeroPascal(n, k))
            elif k == 0:
                print(" "*(linhas-linhaAtual), numeroPascal(n, k), end="  ")
                return trianguloPascal2(linhas, linhaAtual, n, k + 1, quant + 1)
            else:
                print(numeroPascal(n, k), end="  ")
                return trianguloPascal2(linhas, linhaAtual, n, k + 1, quant + 1)
        elif linhaAtual == 1:
            print(" "*(linhas-1), numeroPascal(n, k))
        elif quant == linhaAtual:
            print(numeroPascal(n, k))
        elif k == 0:
            print(" "*(linhas-linhaAtual), numeroPascal(n, k), end=" ")
            return trianguloPascal2(linhas, linhaAtual, n, k + 1, quant + 1)
        else:
            print(numeroPascal(n, k), end=" ")
            return trianguloPascal2(linhas, linhaAtual, n, k + 1, quant + 1)
        return trianguloPascal2(linhas, linhaAtual + 1, n = linhaAtual, k = 0, quant = 1)

trianguloPascal2(10)