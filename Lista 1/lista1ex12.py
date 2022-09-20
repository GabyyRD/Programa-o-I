l = int(input("Digite o número de lados do polígono: "))
m = int(input("Digite a medida dos lados: "))
if l == 3:
    print(f"Triângulo {3*m}")
elif l == 4:
    print(f"Quadrdado {m**2}")
elif l == 5:
    print(f"Pentagono")
elif l != 3 or l != 4 or l != 5:
    print("Polígono não identificado")