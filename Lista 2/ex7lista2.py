def ehTriangulo(a, b, c):
    if abs(b - c) < a < b + c:
        return True
    elif abs(a - c) < b < a + c:
        return True
    elif abs(a - b) < c < a + b:
        return True
    return False

def tipoTriangulo(a, b, c, d):
    if d == False:
        print("Não é um triângulo")
    elif a == b == c:
        print("Triângulo equilátero")
    elif a == b != c or a == c != b or b == c != a:
        print("Triângulo isósceles")
    elif a != b != c:
        print("Triâgulo escaleno")

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    tipoTriangulo(a, b, c, ehTriangulo(a, b, c))

main()
