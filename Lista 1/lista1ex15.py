ano = int(input("Digite um ano: "))
if 1582 <= ano <= 1699:
    X = 22
    Y = 2
elif 1700 <= ano <= 1799:
    X = 23
    Y = 3
elif 1800 <= ano <= 1899:
    X = 23
    Y = 4
elif 1900 <= ano <= 1999:
    X = 24
    Y = 5
elif 2000 <= ano <= 2099:
    X = 24
    Y = 5
elif 2100 <= ano <= 2199:
    X = 24
    Y = 6
elif 2200 <= ano <= 2299:
    X = 25
    Y = 0
elif 2300 <= ano <= 2399:
    X = 26
    Y = 1
elif 2400 <= ano <= 2499:
    X = 25
    Y = 1
a = ano % 19
b = ano % 4
c = ano % 7
d = (19 * a + X) % 30
e = (2 * b + 4 * c + 6 * d + Y) % 7
P1 = 22 + d + e
P2 = d + e - 9
P3 = P2 - 7
if P1 <= 31:
    print(f"Em {ano} a Páscoa foi ou será em {P1} de Março")
elif P2 <= 25:
    print(f"Em {ano} a Páscoa foi ou será em {P2} de Abril")
else:
    print(f"Em {ano} a Páscoa foi ou será em {P3} de Abril")