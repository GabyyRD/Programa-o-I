print("Tempo do corredor 1")
h = int(input("   -> Quantas horas? "))
m = int(input("   -> Quantos minutos? "))
s = int(input("   -> Quantos segundos? "))
print("Tempo do corredor 2")
h2 = int(input("   -> Quantas horas? "))
m2 = int(input("   -> Quantos minutos? "))
s2 = int(input("   -> Quantos segundos? "))

tempo1 = (h*3600) + (m*60) + s
tempo2 = (h2*3600) + (m2*60) + s2

if tempo1 < tempo2:
    diferenca = tempo2 - tempo1
    print("Vencedor: corredor 1")
else:
    diferenca = tempo1 - tempo2
    print("Vencedor: corredor 2")

htempo = diferenca//3600
mtempo = (diferenca%3600)//60
stempo = (diferenca%3600)%60

print(f"Diferença: {htempo} horas {mtempo} minutos {stempo} segundos")