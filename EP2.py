import random
from os import scandir, system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2022100301" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Gabrielly Rosário" 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def imprimeTabuleiro(L):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    RST     = '\033[00m'
    On_White = '\033[47m'
    print(f"\n{On_White} {L[7]} | {L[8]} | {L[9]} {RST}")
    print(f"{On_White}---+---+---{RST}")
    print(f"{On_White} {L[4]} | {L[5]} | {L[6]} {RST}")
    print(f"{On_White}---+---+---{RST}")
    print(f"{On_White} {L[1]} | {L[2]} | {L[3]} {RST}")

def empate(L):
    """Informa se houve empate ou não."""
    if " " not in L:
        return True
    return False

def ganhador(L, simbolo):
    """ Mostra se houve alguém que ganhou. Isso é reconhecido se tiver o mesmo simbolo nos 3 espaços
    de uma linha, coluna ou diagonal formada com a lista recebida como parâmetro.
    se houver vencedor, retorna True, caso contrário, retorna False."""
    if L[1] == L[2] == L[3] == simbolo or L[4] == L[5] == L[6] == simbolo or L[7] == L[8] == L[9] == simbolo or L[1] == L[5] == L[9] == simbolo:
        return True
    elif L[1] == L[4] == L[7] == simbolo or L[2] == L[5] == L[8] == simbolo or L[3] == L[6] == L[9] == simbolo or L[3] == L[5] == L[7] == simbolo:
        return True
    return False


def espaco(L, i = 0, quant = 0):
    """Recebe a lista e verifica quantos eespaços vazios há nela passando por todas as
    posições através da variável contadora."""
    if i < len(L):
        if L[i] == " ":
            return espaco(L, i + 1, quant + 1)
        else:
            return espaco(L, i + 1, quant)
    return quant


def jogada(L, primeiro, simboloComputador, simboloJogador):
    """Recebe a lista de posições, o primeiro jogador da partida e seus símbolos.
    Passa pelas funções que escolhem os valores do computador e do jogador e após cada uma delas, verifica se houve ganhador ou empate.
    Após isso, a função é chamada de novo."""
    if ganhador(L, simboloJogador):
        print("\nParabéns, você venceu!")
        imprimeTabuleiro(L)
        exit()
    elif ganhador(L, simboloComputador):
        print("\nComputador venceu")
        imprimeTabuleiro(L)
        exit()
    elif empate(L):
        print("\nEmpate")
        imprimeTabuleiro(L)
        exit()
    if primeiro == "jogador":
        imprimeTabuleiro(L)
        L[jogadaJogador(L, simboloJogador)] = simboloJogador
        if ganhador(L, simboloJogador):
            print("\nParabéns, você venceu!")
            imprimeTabuleiro(L)
            exit()
        elif empate(L):
            print("\nEmpate")
            imprimeTabuleiro(L)
            exit()
        else:
            L[jogadaComputador(L, simboloComputador)] = simboloComputador
            if ganhador(L, simboloComputador):
                print("\nComputador venceu")
                imprimeTabuleiro(L)
                exit()
            elif empate(L):
                print("\nEmpate")
                imprimeTabuleiro(L)
                exit()
    elif primeiro == "computador":
        L[jogadaComputador(L, simboloComputador)] = simboloComputador
        imprimeTabuleiro(L)
        if ganhador(L, simboloComputador):
            print("\nComputador venceu")
            imprimeTabuleiro(L)
            exit()
        elif empate(L):
            print("\nEmpate")
            imprimeTabuleiro(L)
            exit()
        else:
            L[jogadaJogador(L, simboloJogador)] = simboloJogador
            if ganhador(L, simboloJogador):
                print("\nParabéns, você venceu!")
                imprimeTabuleiro(L)
                exit()
            elif empate(L):
                print("\nEmpate")
                imprimeTabuleiro(L)
                exit()
    jogada(L, primeiro, simboloComputador, simboloJogador)

def jogadaComputador(L, simboloComputador):
    """Função que recebe o tabuleiro e o símbolo do computador e retorna sua posição"""
    # Jogada inicial se a partida começar com o computador:
    if espaco(L) == 9:
        return random.choice([1, 3, 7, 9])

    #jogada final para ganhar:
    elif L[2] == simboloComputador and L[3] == simboloComputador and L[1] == " " or L[4] == simboloComputador and L[7] == simboloComputador and L[1] == " " or L[5] == simboloComputador and L[9] == simboloComputador and L[1] == " ":
        return 1 
    elif L[1] == simboloComputador and L[3] == simboloComputador and L[2] == " " or L[5] == simboloComputador and L[8] == simboloComputador and L[2] == " ":
        return 2
    elif L[1] == simboloComputador and L[2] == simboloComputador and L[3] == " " or L[5] == simboloComputador and L[7] == simboloComputador and L[3] == " " or L[6] == simboloComputador and L[9] == simboloComputador and L[3] == " ":
        return 3
    elif L[1] == simboloComputador and L[7] == simboloComputador and L[4] == " " or L[5] == simboloComputador and L[6] == simboloComputador and L[4] == " ":
        return 4
    elif L[1] == simboloComputador and L[9] == simboloComputador and L[5] == " " or L[2] == simboloComputador and L[8] == simboloComputador and L[5] == " " or L[7] == simboloComputador and L[3] == simboloComputador and L[5] == " " or L[4] == simboloComputador and L[6] == simboloComputador and L[5] == " ":
        return 5
    elif L[3] == simboloComputador and L[9] == simboloComputador and L[6] == " " or L[4] == simboloComputador and L[5] == simboloComputador and L[6] == " ":
        return 6
    elif L[1] == simboloComputador and L[4] == simboloComputador and L[7] == " " or L[3] == simboloComputador and L[5] == simboloComputador and L[7] == " " or L[8] == simboloComputador and L[9] == simboloComputador and L[7] == " ":
        return 7
    elif L[7] == simboloComputador and L[9] == simboloComputador and L[8] == " " or L[2] == simboloComputador and L[5] == simboloComputador and L[8] == " ":
        return 8
    elif L[1] == simboloComputador and L[5] == simboloComputador and L[9] == " " or L[3] == simboloComputador and L[6] == simboloComputador and L[9] == " " or L[7] == simboloComputador and L[8] == simboloComputador and L[9] == " ":
        return 9

    #Jogada para bloquear:
    if (L[2] != simboloComputador and L[3] != simboloComputador and L[2] != " " and L[3] != " " and L[1] == " ") or (L[4] != simboloComputador and L[7] != simboloComputador and L[4] != " " and L[7] != " " and L[1] == " ") or (L[5] != simboloComputador and L[9] != simboloComputador and L[5] != " " and L[9] != " " and L[1] == " "):
        return 1
    elif (L[1] != simboloComputador and L[3] != simboloComputador and L[1] != " " and L[3] != " " and L[2] == " ") or (L[5] != simboloComputador and L[8] != simboloComputador and L[5] != " " and L[8] != " " and L[2] == " "):
        return 2
    elif (L[1] != simboloComputador and L[2] != simboloComputador and L[1] != " " and L[2] != " " and L[3] == " ") or (L[5] != simboloComputador and L[7] != simboloComputador and L[5] != " " and L[7] != " " and L[3] == " ") or (L[6] != simboloComputador and L[9] != simboloComputador and L[6] != " " and L[9] != " " and L[3] == " "):
        return 3
    elif (L[1] != simboloComputador and L[7] != simboloComputador and L[1] != " " and L[7] != " " and L[4] == " ") or (L[5] != simboloComputador and L[6] != simboloComputador and L[5] != " " and L[6] != " " and L[4] == " "):
        return 4
    elif (L[1] != simboloComputador and L[9] != simboloComputador and L[1] != " " and L[9] != " " and L[5] == " ") or (L[4] != simboloComputador and L[6] != simboloComputador and L[4] != " " and L[6] != " " and L[5] == " "):
        return 5
    elif (L[7] != simboloComputador and L[3] != simboloComputador and L[7] != " " and L[3] != " " and L[5] == " ") or (L[2] != simboloComputador and L[8] != simboloComputador and L[2] != " " and L[8] != " " and L[5] == " "):
        return 5
    elif (L[3] != simboloComputador and L[9] != simboloComputador and L[3] != " " and L[9] != " " and L[6] == " ") or (L[4] != simboloComputador and L[5] != simboloComputador and L[4] != " " and L[5] != " " and L[6] == " "):
        return 6
    elif (L[1] != simboloComputador and L[4] != simboloComputador and L[1] != " " and L[4] != " " and L[7] == " ") or (L[3] != simboloComputador and L[5] != simboloComputador and L[3] != " " and L[5] != " " and L[7] == " ") or (L[8] != simboloComputador and L[9] != simboloComputador and L[8] != " " and L[9] != " " and L[7] == " "):
        return 7
    elif (L[2] != simboloComputador and L[5] != simboloComputador and L[2] != " " and L[5] != " " and L[8] == " ") or (L[7] != simboloComputador and L[9] != simboloComputador and L[7] != " " and L[9] != " " and L[8] == " "):
        return 8
    elif (L[1] != simboloComputador and L[5] != simboloComputador and L[1] != " " and L[5] != " " and L[9] == " ") or (L[3] != simboloComputador and L[6] != simboloComputador and L[3] != " " and L[6] != " " and L[9] == " ") or (L[7] != simboloComputador and L[8] != simboloComputador and L[7] != " " and L[8] != " " and L[9] == " "):
        return 9

    # 2º jogada do computador em uma partida que começou com ele
        #Se o jogador adversário jogar no meio:
    elif espaco(L) == 7 and L[5] != simboloComputador and L[5] != " " and L[1] == simboloComputador:
        return 9
    elif espaco(L) == 7 and L[5] != simboloComputador and L[5] != " " and L[3] == simboloComputador:
        return 7
    elif espaco(L) == 7 and L[5] != simboloComputador and L[5] != " " and L[7] == simboloComputador:
        return 3
    elif espaco(L) == 7 and L[5] != simboloComputador and L[5] != " " and L[9] == simboloComputador:
        return 1
        #Se o jogador adversário jogar ao lado do computador:
    elif espaco(L) == 7 and L[2] != simboloComputador and L[2] != " " and L[1] == simboloComputador:
        return 7
    elif espaco(L) == 7 and L[4] != simboloComputador and L[4] != " " and L[1] == simboloComputador:
        return 3
    elif espaco(L) == 7 and L[2] != simboloComputador and L[2] != " " and L[3] == simboloComputador:
        return 9
    elif espaco(L) == 7 and L[6] != simboloComputador and L[6] != " " and L[3] == simboloComputador:
        return 1
    elif espaco(L) == 7 and L[8] != simboloComputador and L[8] != " " and L[7] == simboloComputador:
        return 1
    elif espaco(L) == 7 and L[4] != simboloComputador and L[4] != " " and L[7] == simboloComputador:
        return 9
    elif espaco(L) == 7 and L[8] != simboloComputador and L[8] != " " and L[9] == simboloComputador:
        return 3
    elif espaco(L) == 7 and L[6] != simboloComputador and L[6] != " " and L[9] == simboloComputador:
        return 7

    # 1ª jogada do computador se a partida tiver começado com o jogador:
    elif espaco(L) == 8 and L[5] == " ":
        return 5
    
    # 2ª jogada do computador se a partida tiver começado com ele:
    elif espaco(L) == 7 and L[5] != " " and L[5] != simboloComputador and L[1] == simboloComputador:
        return 9
    elif espaco(L) == 7 and L[5] != " " and L[5] != simboloComputador and L[3] == simboloComputador:
        return 7
    elif espaco(L) == 7 and L[5] != " " and L[5] != simboloComputador and L[7] == simboloComputador:
        return 3
    elif espaco(L) == 7 and L[5] != " " and L[5] != simboloComputador and L[9] == simboloComputador:
        return 1

    # 2ª jogada do computador se a partida tiver começado com o jogador:
    elif espaco(L) == 6 and L[1] == L[9] != " " and L[1] == L[9] != simboloComputador:
        return 2
    elif espaco(L) == 6 and L[3] == L[7] != " " and L[3] == L[7] != simboloComputador:
        return 2
    elif espaco(L) == 6 and L[1] == L[8] != " " and L[1] == L[8] != simboloComputador:
        return 7
    elif espaco(L) == 6 and L[1] == L[6] != " " and L[1] == L[6] != simboloComputador:
        return 3
    elif espaco(L) == 6 and L[3] == L[8] != " " and L[3] == L[8] != simboloComputador:
        return 9
    elif espaco(L) == 6 and L[3] == L[4] != " " and L[3] == L[4] != simboloComputador:
        return 1
    elif espaco(L) == 6 and L[7] == L[2] != " " and L[7] == L[2] != simboloComputador:
        return 1
    elif espaco(L) == 6 and L[7] == L[4] != " " and L[7] == L[4] != simboloComputador:
        return 9
    elif espaco(L) == 6 and L[9] == L[2] != " " and L[9] == L[2] != simboloComputador:
        return 3
    elif espaco(L) == 6 and L[9] == L[4] != " " and L[9] == L[4] != simboloComputador:
        return 2
    elif espaco(L) == 6 and L[2] == L[4] != " " and L[2] == L[4] != simboloComputador and L[5] == simboloComputador:
        return 1
    elif espaco(L) == 6 and L[2] == L[6] != " " and L[2] == L[6] != simboloComputador and L[5] == simboloComputador:
        return 3
    elif espaco(L) == 6 and L[4] == L[8] != " " and L[4] == L[8] != simboloComputador and L[5] == simboloComputador:
        return 7
    elif espaco(L) == 6 and L[6] == L[8] != " " and L[6] == L[8] != simboloComputador and L[5] == simboloComputador:
        return 9

    # 3ª jogada do computador se a partida tiver começado com ele.
    elif espaco(L) == 5 and L[1] == L[7] == simboloComputador and L[2] == L[4] != simboloComputador and L[2] == L[4] != " ":
        return 9
    elif espaco(L) == 5 and L[1] == L[3] == simboloComputador and L[2] == L[4] != simboloComputador and L[2] == L[4] != " ":
        return 9
    elif espaco(L) == 5 and L[3] == L[9] == simboloComputador and L[2] == L[6] != simboloComputador and L[2] == L[6] != " ":
        return 7
    elif espaco(L) == 5 and L[1] == L[3] == simboloComputador and L[2] == L[6] != simboloComputador and L[2] == L[6] != " ":
        return 7
    elif espaco(L) == 5 and L[1] == L[7] == simboloComputador and L[4] == L[8] != simboloComputador and L[4] == L[8] != " ":
        return 3
    elif espaco(L) == 5 and L[7] == L[9] == simboloComputador and L[4] == L[8] != simboloComputador and L[4] == L[8] != " ":
        return 3
    elif espaco(L) == 5 and L[3] == L[9] == simboloComputador and L[6] == L[8] != simboloComputador and L[6] == L[8] != " ":
        return 1
    elif espaco(L) == 5 and L[7] == L[9] == simboloComputador and L[6] == L[8] != simboloComputador and L[6] == L[8] != " ":
        return 1

    # Jogadas finais caso não tenha se encaixado em nenhuma das anteriores (improvável, mas não corre o risco de retornar None)
    elif L[1] == " ":
        return 1
    elif L[3] == " ":
        return 3
    elif L[7] == " ":
        return 7
    elif L[9] == " ":
        return 9
    elif L[5] == " ":
        return 5
    elif L[2] == " ":
        return 2
    elif L[4] == " ":
        return 4
    elif L[6] == " ":
        return 6
    elif L[8] == " ":
        return 8
    else:
        return random.randint(1,9)

def jogadaJogador(L, simboloJogador):
    """Jogada da pessoa. Recebe o tabuleiro e os simbolos do jogador e computador, respectivamente.
    Identifica se o valor digitado é válido e está no limite (entre 1 e 9). Caso seja um valor válido, 
    envia-o à função posicão para ver se é possível ficar com ela."""
    try:
        escolha = int(input("\nQual posição deseja marcar? "))
        if escolha < 1 or escolha > 9:
            print("\nValor inválido. Você deve digitar um número inteiro entre 1 e 9.")
            return escolha
        else:
           return posicao(L, escolha, simboloJogador)
    except:
        print("Tipo inválido.")
        return jogadaJogador(L, simboloJogador)

def posicao(L, escolha, simboloJogador):
    """Recebe o tabuleiro, a posição escolhida e o simbolo do jogador.
    Se a posição não estiver disponível, avisa e retorna à função jogadaJogador.
    Se não, retorna o valor."""
    if L[escolha] != " ":
        print("\nNão é possível escolher este local.")
        return jogadaJogador(L, simboloJogador)
    else:
        return escolha

def escolhas():
    """Pede o símbolo do jogador, verifica se é válido e sorteia quem começa a partida."""
    On_White = '\033[47m'
    RST = '\033[00m'
    print(f"\n{On_White}SEJA BEM-VINDO AO JOGO DA VELHA!{RST}\n")
    simbolo = input(f"Qual símbolo você será? {On_White} X {RST} ou {On_White} 0 {RST} ? ")
    if simbolo != "X" and simbolo != "x" and simbolo != "O" and simbolo != "o" and simbolo != 0 and simbolo != "0":
        print("Símbolo inválido!")
        return escolhas()
    else:
        L = [" "] * 10
        L[0] = "*"
        começa = random.randint(0,1)
        if começa == 0:
            print("Muito bem! Nesta rodada você começa.")
            if simbolo == "X" or simbolo == "x":
                jogada(L, "jogador", "O", "X")
            else:
                jogada(L, "jogador", "X", "O")
        else:
            print("Neste rodada o computador começa.")
            if simbolo == "X" or simbolo == "x":
                jogada(L, "computador", "O", "X")
            else:
                jogada(L, "computador", "X", "O")

def main():
    limpaTela()
    print(getNome())
    print(getMatricula())
    escolhas()



################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()