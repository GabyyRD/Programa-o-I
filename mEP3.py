######################################################
# Programação I / Programação Funcional (2022/1)
# miniEP3 - Ironman
# Nome: Gabrielly Rosário Dionisio
# Matrícula: 2022100301
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do
#   Paradigma Funcional.
# - Você NÃO pode usar variáveis globais;
# - Não use funções recursivas (não há necessidade);
# - Caso precise, você PODE criar outras funções;
# - Evite ao máximo a replicação de código. 
#   Códigos que não atendam a esse requisito 
#   valerão 50% da pontuação;
######################################################

def tempoindicem():
    """
    Recebe a idade do atleta de sexo masculino e mostra qual o tempo mínimo que o atleta pode levar para participar da competição.
    """
    id = int(input())
    if 18 <= id <= 29:
        return int(480)
    elif 30 <= id <= 34:
        return int(490)
    elif 35 <= id <= 39:
        return int(505)
    elif 40 <= id <= 44:
        return int(515)
    elif 45 <= id <= 49:
        return int(530)
    elif 50 <= id <= 54:
        return int(540)
    elif 55 <= id <= 59:
        return int(555)
    elif 60 <= id <= 64:
        return int(570)
    elif 65 <= id <= 69:
        return int(590)
    elif 70 <= id <= 74:
        return int(620)
    elif 75 <= id <= 79:
        return int(660)
    elif id >= 80:
        return int(720)

def tempoindicef():
    """
    Recebe a idade da atleta de sexo feminino e mostra qual o tempo mínimo que o atleta pode levar para participar da competição.
    """
    id = int(input())
    if 18 <= id <= 29:
        return int(490)
    elif 30 <= id <= 34:
        return int(500)
    elif 35 <= id <= 39:
        return int(520)
    elif 40 <= id <= 44:
        return int(540)
    elif 45 <= id <= 49:
        return int(560)
    elif 50 <= id <= 54:
        return int(580)
    elif 55 <= id <= 59:
        return int(600)
    elif 60 <= id <= 64:
        return int(630)
    elif 65 <= id <= 69:
        return int(660)
    elif 70 <= id <= 74:
        return int(705)
    elif 75 <= id <= 79:
        return int(750)
    elif id>= 80:
        return int(810)


def tempoatletaminutos():
    """
    Recebe o tempo em minutos de cada modalidade e intervalo e retorna o tempo total que o atleta levou.
    """
    tN = int(input()) #todos em minutos
    t1 = int(input())
    tC = int(input())
    t2 = int(input())
    tCo = int(input())
    return (tN + t1 + tC + t2 + tCo)

def conversaohoras(x):
    """
    Converte minutos em horas
    """
    return x // 60

def conversaominutos(x):
    """
    Apresenta os minutos
    """
    return x % 60

def main():
    """
    Coleta todos os dados das outras funções e retorna o tempo do atleta, o máximo que ele poderia levar, se conseguiu ser aprovado e a diferença de tempo.
    """
    s = input()
    if s == "M" or s == "m":
        y = tempoindicem()
        x = tempoatletaminutos()
        print(f"Tempo do atleta: {conversaohoras(x):02}h {conversaominutos(x):02}min")
        print(f"Tempo necessario: {conversaohoras(y):02}h {conversaominutos(y):02}min")
        if x > y:
            print("Conseguiu indice? NAO")
            print(f"O atleta terminou a prova {(x-y) // 60:02}h {(x-y) % 60:02}min acima do indice")
        elif x <= y:
            print("Conseguiu indice? SIM")
            print(f"O atleta terminou a prova {(y-x) // 60:02}h {(y-x) % 60:02}min abaixo do indice")
    else:
        y = tempoindicef()
        x = tempoatletaminutos()
        print(f"Tempo da atleta: {conversaohoras(x):02}h {conversaominutos(x):02}min")
        print(f"Tempo necessario: {conversaohoras(y):02}h {conversaominutos(y):02}min")
        if x > y:
            print("Conseguiu indice? NAO")
            print(f"A atleta terminou a prova {(x-y) // 60:02}h {(x-y) % 60:02}min acima do indice")
        elif x <= y:
            print("Conseguiu indice? SIM")
            print(f"A atleta terminou a prova {(y-x) // 60:02}h {(y-x) % 60:02}min abaixo do indice")

main()
