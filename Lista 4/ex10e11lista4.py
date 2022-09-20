def ehVogal(caractere):
    vogais = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    if caractere in vogais:
        return True
    return False

def contaVogal(string, i = 0, vogais = 0):
    if i == len(string):
        return vogais
    elif ehVogal(string[i]) == True:
        return contaVogal(string, i + 1, vogais + 1)
    return contaVogal(string, i + 1, vogais)

def contaConsoante1(string, i = 0, consoantes = 0):
    """Utilizando a função ehVogal."""
    if i == len(string):
        print(f"Número de consoantes: {consoantes}.")
        return 
    elif ehVogal(string[i]) == False:
        return contaConsoante1(string, i + 1, consoantes + 1)
    return contaConsoante1(string, i + 1, consoantes)

def contaConsoante2(string, vogais):
    """Utilizando a função contaVogal."""
    consoantes = len(string) - vogais
    print(f"Número de consoantes: {consoantes}.")

def main():
    string = input()
    print(f"Número de vogais: {contaVogal(string)}")
    contaConsoante1(string)
    contaConsoante2(string, contaVogal(string))
    
main()