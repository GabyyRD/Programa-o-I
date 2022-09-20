documento_autorização = str()
meses = int()
numero_doacoes = int()
sexo_biologico = str()
gravidez = str()
amamentando = str()
meses_bebe = int()
peso = float(input())
idade = int(input())
if idade == 16 or idade == 17:
    documento_autorização = input()  # S ou N - se for menor de 18
boa_saude = input() # S ou N
drogas = input() # S ou N
primeira_doacao = input() # S ou N
if primeira_doacao == "N":
    meses = int(input()) # só para doador, intervalo mínimo entre as doações
    numero_doacoes = int(input()) # só para doador, numero anual
sexo_biologico = input() # M ou F
if sexo_biologico == "F":
    gravidez = input() # S ou N, para sexo feminino
    amamentando = input() # S ou N, para sexo feminino
    if amamentando == "S":
        meses_bebe = int(input()) # para quem amamenta
print(f"Peso: {peso}")
print(f"Idade: {idade}")
if idade == 16 or idade == 17:
    print(f"Documento de autorizacao: {documento_autorização}")
print(f"Boa saude: {boa_saude}")
print(f"Uso drogas injetaveis: {drogas}")
print(f"Primeira doacao: {primeira_doacao}")
if primeira_doacao == "N":
    print(f"Meses desde ultima doacao: {meses}")
    print(f"Doacoes nos ultimos 12 meses: {numero_doacoes}")
print(f"Sexo biologico: {sexo_biologico}")
if sexo_biologico == "F":
    print(f"Gravidez: {gravidez}")
    print(f"Amamentando: {amamentando}")
    if amamentando == "S":
        print(f"Meses bebe: {meses_bebe}")
hemocentro = True
if peso < 50:
    hemocentro = False
    print("Impedimento: abaixo do peso minimo.")
if idade < 16:
    hemocentro = False
    print("Impedimento: menor de 16 anos.")
if idade == 16 and documento_autorização == "N":
    hemocentro = False
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
if idade == 17 and documento_autorização == "N":
    hemocentro = False
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
if idade >= 60 and idade <= 69 and primeira_doacao == "S":
    hemocentro = False
    print("Impedimento: maior de 60 anos, primeira doacao.")
if idade > 69:
    hemocentro = False
    print("Impedimento: maior de 69 anos.")
if boa_saude == "N":
    hemocentro = False
    print("Impedimento: nao esta em boa saude.")
if drogas == "S":
    hemocentro = False
    print("Impedimento: uso de drogas injetaveis.")
if sexo_biologico == "F" and primeira_doacao == "N" and meses <= 3: 
    hemocentro = False
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
if sexo_biologico == "F" and primeira_doacao == "N" and numero_doacoes >= 3:
    hemocentro = False
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
if sexo_biologico == "M" and primeira_doacao == "N" and meses <= 2:
    hemocentro = False
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
if sexo_biologico == "M" and primeira_doacao == "N" and numero_doacoes >= 4:
    hemocentro = False
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
if gravidez == "S":
    hemocentro = False
    print("Impedimento: gravidez.")
if amamentando == "S" and meses_bebe < 12:
    hemocentro = False
    print("Impedimento: amamentacao.")
if hemocentro:
    print("Procure um hemocentro.")