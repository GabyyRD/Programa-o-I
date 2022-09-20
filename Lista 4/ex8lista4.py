from math import sqrt 

def leTemperaturas(n, T = []):
    if len(T) == n:
        media(T)
    else:
        temp = int(input())
        T += [temp]
        return leTemperaturas(n, T)

def media(T, i = 0, s = 0):
    if i < len(T):
        s += T[i]
        return media(T, i + 1, s)
    else:
        m = s/len(T)
        print(f"Média das temperaturas: {m}")
        desvio(m, T)

def desvio(media, T, i = 0, s = 0):
    if i == len(T):
        dp = sqrt((1/len(T)*s))
        print(f"Desvio padrão: {dp}")
    else:
        s += (T[i] - media)**2
        return desvio(media, T, i + 1, s)
    

def main():
    n = int(input("Digite quantos dias a temperatura será analizada: "))
    leTemperaturas(n)

main()
