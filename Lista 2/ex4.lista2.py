def converte(h, m, s, d):
    soma = h*60 + m + s/60
    ritmo = int(soma//d)
    sritmo = round((soma/d - soma//d)*60)
    print(f"--> Ritmo: {ritmo:02}:{sritmo:02} min/km")

def main():
    print("Tempo do corredor (horas, minutos e segundos):")
    h = int(input())
    m = int(input())
    s = int(input())
    d = float(input("Distância percorrida (em km): "))
    converte(h, m, s, d)

main()