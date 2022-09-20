print("Digite a data de nascimento:")
d = int(input("    -> Dia? "))
m = int(input("    -> Mês? "))
a = int(input("    -> Ano? "))
print("Digite a data atual:")
d2 = int(input("    -> Dia? "))
m2 = int(input("    -> Mês? "))
a2 = int(input("    -> Ano? "))
if m == m2 and d > d2 or m > m2:
    print(f"{a2 - a - 1} anos")
else:
    print(f"{a2 - a} anos")