from math import factorial

def euler(n):
    if n > 0:
        return (1/factorial(n-1)) + euler(n-1)
    return 0

def main():
    n = int(input("Número de termos: "))
    print(f"Resultado: {euler(n):.5f}")

main()