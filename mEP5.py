L = ["Brancos","Maria", "José", "Carlos", "Marta", "Nulos"]
R = [1, 2, 3, 0, 5, 1]


def maior(L, R, i = 0, c = 0):
    if i >= len(L) - 1:
        print(R[i])
        print(c)
        print(f"Vencedor: {L[c]}")
    elif R[i] > R[i+1]:
        return maior(L, R, i+1, c = R[i])
    else:
        return maior(L, R, i +1, c = R[i +1])

def maior2(L, R, i=0, maior=-1):
    if i == len(L):
        print(f"Vencedor: {L[maior]}")
    elif R[i] > R[maior]:
        return maior2(L, R, i+1, maior = i)
    else:
        return maior2(L, R, i +1, maior)

maior2(L, R)

def vence(L, R):
    x = max(R)
    print(x)
    print(R[x])
    print(f"Vence: {L[R[x]]}")





def  maior1(L, R, i=0, maior=0):
    if i >= len(L) - 1:
        print(R[i])
        print(maior)
        print(f"Vencedor: {L[maior]}")
    elif R[i] > R[i+1]:
        if R[i] > R[i+2]:
            return maior1(L, R, i+1, maior= R[i])
        else:
            return maior1(L, R, i +1, R=[i+2])
    else:
        return maior1(L, R, i +1, maior = R[i+1])

