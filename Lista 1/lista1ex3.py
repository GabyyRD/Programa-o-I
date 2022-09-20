t = int(input("Digite o tempo total gasto na corrida (em min): "))
d = int(input("Digite a distância percorrida (em km): "))
ritmo_médio= t/d
ritmo_médio=int(ritmo_médio)
s = (t%d)*6
print(f"Ritmo médio do corredor: {ritmo_médio}:{s} min/km.")