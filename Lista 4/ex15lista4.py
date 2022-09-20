import math as m

def trapezio(funcao, a, b, n, i = 0, soma = 0):
    """Função que implementa a Regra dos Trapézios para encontrar o valor de uma integral definida."""
    deltaX = (b - a)/n
    xi = a + i * deltaX
    if i > n:
        return (deltaX/2)*soma
    elif i == 0 or i == n:
        soma += funcao(xi)
        return trapezio(funcao, a, b, n, i + 1, soma)
    else:
        soma += 2 * funcao(xi)
        return trapezio(funcao, a, b, n, i + 1, soma)

def funcao1(x):
    return x**2 + x + 2

def funcao2(x):
    return m.exp(x)

def main():
    print(trapezio(funcao1, 0, 10, 10))
    print(trapezio(funcao2, -10, 10, 100))
    print(trapezio(lambda x: m.sqrt(x) + m.exp(x), 5, 10, 100))
    print(trapezio(lambda x: m.log(x)**3/x, 1, 15, 100))
    print(trapezio(lambda x: m.sin(x), 0, m.pi, 5))
    print(trapezio(lambda x: m.sin(x), 0, m.pi, 10))
    print(trapezio(lambda x: m.sin(x), 0, m.pi, 50))
    print(trapezio(lambda x: m.sin(x), 0, m.pi, 500))
    print(trapezio(lambda x: m.sin(x), 0, m.pi, 900))
    print(trapezio(lambda a: m.sin(a)**2 + 2 * m.sin(2*a)**4, 0, m.pi, 500))

main()


