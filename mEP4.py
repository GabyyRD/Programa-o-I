######################################################
# Programação I / Programação Funcional (2022/1)
# miniEP4 - Jogo da Velha
# Nome: Gabrielly Rosário Dionisio
# Matrícula: 2022100301
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do 
#   Paradigma Funcional.
# - Você não pode usar variáveis globais;
# - Não use funções recursivas (não há necessidade);
# - Você deve seguir o código base disponibilizado, 
#   não sendo permitido a alteração do nome e/ou
#   lista de parâmetros das funções dadas;
# - Caso precise, você PODE criar outras funções;
# - Não é permitido a utilização de lista, tuplas 
#   ou qualquer outro tipo estruturado para 
#   “facilitar” a manipulação dos dados. Você deve 
#   sempre trabalhar com as 9 variáveis que 
#   representam as posições no tabuleiro;
#
# Dica: Leia o docstring de cada função para saber o
#       que cada uma deve fazer e retornar.
######################################################

def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    print(f" {p7} | {p8} | {p9} ")
    print("---+---+---")
    print(f" {p4} | {p5} | {p6} ")
    print("---+---+---")
    print(f" {p1} | {p2} | {p3} ")

def s(simbolo):
    """
    Verifica se os símbolos estão corrertos
    """
    if simbolo == "x" or simbolo == "o" or simbolo == " ":
        return True
    return False

def ganhador(a, p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Vê para a função verificaJogada quem ganhou"""
    if p1 == p2 == p3 == a or p4 == p5 == p6 == a or p7 == p8 == p9 == a or p3 == p5 == p7 == a:
        return a
    elif p1 == p4 == p7 == a or p2 == p5 == p8 == a or p3 == p6 == p9 == a or p1 == p5 == p9 == a:
        return a


def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    if s(p1) and s(p2) and s(p3) and s(p4) and s(p5) and s(p6) and s(p7) and s(p8) and s(p9):
        return True
    return False

def contarJogadas(a, p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Conta a quantidade de jogadas que possuem o mesmo símbolo que estiver na variável a.
    """
    cont = 0
    if p1 == a:
        cont += 1
    if p2 == a:
        cont += 1
    if p3 == a:
        cont += 1
    if p4 == a:
        cont += 1
    if p5 == a:
        cont += 1
    if p6 == a:
        cont += 1
    if p7 == a:
        cont += 1
    if p8 == a:
        cont += 1
    if p9 == a: 
        cont += 1
    return cont

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e verifica se os valores formam uma jogada válida.
    Retorna True se a jogada for válida e False, caso contrário
    """
    if abs(contarJogadas("x", p1, p2, p3, p4, p5, p6, p7, p8, p9) - contarJogadas("o", p1, p2, p3, p4, p5, p6, p7, p8, p9)) > 1:
        return False
    return True


def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    if ganhador("x", p1, p2, p3, p4, p5, p6, p7, p8, p9):
        print("O jogador 'x' venceu!")
    elif ganhador("o", p1, p2, p3, p4, p5, p6, p7, p8, p9):
        print("O jogador 'o' venceu!")
    elif p1 == " " or p2 == " " or p3 == " " or p4 == " " or p5 == " " or p6 == " " or p7 == " " or p8 == " " or p9 == " ":
        print("O jogo nao terminou!")
    else:
        print("Empate!")

def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()
