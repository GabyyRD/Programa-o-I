nota1 = float(input("Digite a nota da sua primeira prova: "))
nota2 = float(input("Digite a nota da sua segunda prova: "))
nota3 = float(input("Digite a nota da sua terceira prova: "))
media = (nota1 + nota2+ nota3)/3
if media >= 7.0:
    print("Aluno aprovado")
else:
    print("Precisa fazer Prova Final")
    provafinal = float(input("Digite a nota da sua prova final: "))
    mediafinal = (media + provafinal)/2
    if mediafinal >= 5.0:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")