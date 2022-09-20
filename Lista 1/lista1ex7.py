n = int(input("Digite um número: "))
c = n//100
d = (n - (c*100))//10
u = n - (c*100 + d*10)
if n < 100 or n > 900:
    print("Erro.")
elif c < d < u:
    print(f"{n} é ascendente.")
else:
    print(f"{n} não é ascendente.")