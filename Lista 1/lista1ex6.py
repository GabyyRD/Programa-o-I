numero = int(input("Digite um número: "))
pn = numero//1000
sn = (numero//100)%10
tn = (numero//10)%10
qn = numero%10
if numero < 1000 or numero > 9999:
    print("Valor fora do limite.")
elif pn == qn and sn == tn:
    print(f"{numero} é palíndromo.")
else:
    print(f"{numero} não é palíndromo.")