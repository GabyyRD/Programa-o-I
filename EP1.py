from cmath import atan
from os import system, name

def limpaTela():
    """Limpa a tela do terminal quando chamada."""
    if name == 'nt':  # Windows
        system('cls')
    else:  # Linux ou outro SO
        system('clear')

def leValor(funcaoConv, msg = "", i = 0):
    """Usada para saber se o cliente está digitando um valor válido. Recebe o tipo da variável, uma mensagem e uma
    variável para contar o número de tentativas"""
    if i >= 5:
        print("\nVocê atingiu o limite de respostas inválidas. Tente novamente na próxima, até mais!")
        exit()
    try:
        return funcaoConv(input(msg))
    except:
        print("ERRO: Tipo inválido\n")
        return leValor(funcaoConv, msg, i + 1)

def menu(a, b, c, d, e, fat):
    """Apresenta o menu da loja, além de receber a quantidade de produtos em estoque e o faturamento.
    Chama a função 'mostrarOpcoes' e 'estoque' para dar continuidade à venda e pede ao cliente o produto escolhido."""
    limpaTela()
    CYAN    = '\033[36m'
    RST     = '\033[00m'
    print(f"\n{CYAN}")
    print("+", 25*"-", "PRODUTOS", 25*"-", "+")
    if a == 0:
        print("||     1 - Brigadeiros", 21*".", "Indisponível     ||")
    else:
        print("||     1 - Brigadeiros", 26*".", "R$10,00     ||")
    if b == 0:
        print("||     2 - Paçocas", 25*".", "Indisponível     ||")
    else:
        print("||     2 - Paçocas", 30*".", "R$12,00     ||")
    if c == 0:
        print("||     3 - Casadinhos", 22*".", "Indisponível     ||")
    else:
        print("||     3 - Casadinhos", 27*".", "R$13,50     ||")
    if d == 0:
        print("||     4 - Cocadas", 25*".", "Indisponível     ||")
    else:
        print("||     4 - Cocadas", 30*".", "R$17,50     ||")
    if e == 0:
        print("||     5 - Cupcakes", 24*".", "Indisponível     ||")
    else:
        print("||     5 - Cupcakes", 29*".", "R$20,00     ||")
    print("+", 23*"-", "OUTRAS OPÇÕES", 22*"-", "+")
    print("||     6 - Informações internas", 25*" ", "    ||")
    print("||     7 - Finalizar", 36*" ", "    ||")
    print("+", 60*"-", "+")
    print(RST)
    opcao = leValor(int, "Escolha uma opção: ")
    estoque(opcao, a, b, c, d, e, fat)

def retornarCompras(a, b, c, d, e, fat, i = 1):
    """Recebe o estoque de produtos, faturamento e um contador de tentativas. Retorna ao menu caso o cliente queira 
    continuar comprando. Se não, apresneta as informações internas e finaliza as compras.."""
    y = input("\nDeseja comprar outro produto? (S/N): ")
    if y == "S" or y == "s":
        menu(a, b, c, d, e, fat)
    elif y == "N" or y == "n":
        estoque(7, a, b, c, d, e, fat)
    else:
        print("\nERRO: Opção inválida")
        if i >= 5: # Número máximo que o cliente pode digitar errado.
            print("\nVocê atingiu o limite de respostas inválidas. Tente novamente na próxima!")
            exit()
        retornarCompras(a, b, c, d, e, fat, i + 1)

def verificaQuantidade(opcao, quant, preco):
    """Recebe a opção do cliente com o valor e a quantidade disponível e avisa se é possível comprar."""
    if quant == 0:
        print(f"\nAcabou.")
    elif opcao == 1:
        print(f"\nVocê escolheu Brigadeiros, perfeito! \nPreço: R${preco:.2f}")
    elif opcao == 2:
        print(f"\nVocê escolheu Paçocas, ótima opção! \nPreço: R${preco:.2f}")
    elif opcao == 3:
        print(f"\nVocê escolheu Casadinhos, perfeito <3 \nPreço: R${preco:.2f}")
    elif opcao == 4:
        print(f"\nVocê escolheu Cocadas, é isso aí ;) \nPreço: R${preco:.2f}")
    elif opcao == 5:
        print(f"\nVocê escolheu Cupcakes, o queridinho <3 \nPreço: R${preco:.2f}")

def escolhas(quant, valor, a, b, c, d, e, fat):
    """Recebe a quantidade do produto escolhido, o estoque dos outros e o valor e faturamento.
    Caso não haja produto disponível, chama a função retornarCompras, senão, confirma a escolha com o cliente."""
    if quant == 0:
        retornarCompras(a, b, c, d, e, fat)
    else:
        _ = input("\n--> Pressione R para retornar ou qualquer outra tecla para confirmar...")
        if _ == "R" or _ == "r":
            menu(a, b, c, d, e, fat)
        else:
            pagar(valor, pagamento(valor))  

def estoque(opcao, a, b, c, d, e, fat):
    """Chama funções que verificarão a disponibilidade de produtos e a atualizaraão, confirmação, retorno às compras. Recebe a quantidade e faturamento 
    e mostra o valor dos produtos, além de modificar a quantidade caso haja o produto disponível chamando funções que realizarão isso."""
    limpaTela()
    br = 10.00
    p = 12.00
    ca = 13.50
    co = 17.50
    cup = 20.00
    #São chamadas funções por ser uma ação com repetição de código e modificação de poucas variáveis.
    if opcao == 1:
        verificaQuantidade(1, a, br)
        escolhas(a, br, a, b, c, d, e, fat)
        retornarCompras(a - 1, b, c, d, e, fat + 10)
    if opcao == 2:
        verificaQuantidade(2, b, p)
        escolhas(b, p, a, b, c, d, e, fat)
        retornarCompras(a, b - 1, c, d, e, fat + 12)
    if opcao == 3:
        verificaQuantidade(3, c, ca)
        escolhas(c, ca, a, b, c, d, e, fat)
        retornarCompras(a, b, c - 1, d, e, fat + 13.50)
    if opcao == 4:
        verificaQuantidade(4, d, co)
        escolhas(d, co, a, b, c, d, e, fat)
        retornarCompras(a, b, c, d - 1, e, fat + 17.50)
    if opcao == 5:
        verificaQuantidade(5, e, cup)
        escolhas(e, cup, a, b, c, d, e, fat)
        retornarCompras(a, b, c, d, e - 1, fat + 20.00)
    if opcao == 6 or opcao == 7:
        limpaTela()
        print("\n            INFORMAÇÕES INTERNAS")
        print("+", 40*"-", "+")
        print(f"  Caixas de brigadeiros disponíveis:     {a}")
        print(f"  Caixas de paçocas disponíveis:         {b}")
        print(f"  Caixas de casadinhos disponíveis:      {c}")
        print(f"  Caixas de cocadas disponíveis:         {d}")
        print(f"  Caixas de cupcakes disponíveis:        {e}")
        print(f"  Faturamento das vendas:         R$ {(fat):.2f}")
        print("+", 40*"-", "+")
        if opcao == 7:
            print("\nObrigado pela preferência. Volte Sempre!!!")
            exit()
        else:
            _ = input("\n--> Pressione qualquer tecla para continuar...")
            retornarCompras(a, b, c, d, e, fat) # A opção 6 mostra as informações e caso nesta função o cliente queira finalizar tudo,
                                                # aparecerá novamente as informações, de forma definitiva.
    else:
        limpaTela()
        input("\nOpção inválida, tente novamente...")
        return menu(a, b, c, d, e, fat)

def pagamento(valor):
    try:
        dinheiro = float(input("\nColoque o dinheiro: "))
        if type(dinheiro) == float:
            if dinheiro < 0:   
                return pagamento(valor)
            else: 
                if dinheiro >= valor:
                    return dinheiro
                else:
                    return dinheiro + pagamento(valor - dinheiro)
    except:
        return pagamento(valor)

def pagar(preço, pago):
    """Apresenta ao cliente os dados relacionados ao pagamento e caso necessário, retorna o troco."""
    dinheiro = pago - preço
    print(f"\nValor pago: {pago:.2f}")
    print(f"Troco: {dinheiro:.2f}")
    if dinheiro > 0:
        print("\nPegue seu troco:")
        troco(dinheiro)

def troco(t): 
    """"Recebe o valor do troco e imprime por cédulas ao cliente."""
    if t >= 100.00:
        print("R$ 100,00")
        return troco(t-100.00)
    elif t >= 50.00:
        print("R$ 50,00")
        return troco(t-50.00)
    elif t >= 20.00:
        print("R$ 20,00")
        return troco(t-20.00)
    elif t >= 10.00:
        print("R$ 10,00")
        return troco(t-10.00)
    elif t >= 5.00:
        print("R$ 5,00")
        return troco(t-5.00)
    elif t >= 2.00:
        print("R$ 2,00")
        return troco(t-2.00)
    elif t >= 1.00:
        print("R$ 1,00")
        return troco(t-1.00)
    elif round(t, 2) >= 0.50:
        print("R$ 0,50")
        return troco(t-0.50)
    elif round(t, 2) >= 0.25:
        print("R$ 0,25")
        return troco(t-0.25)
    elif round(t, 2) >= 0.10:
        print("R$ 0,10")
        return troco(t-0.10)
    elif round(t, 2) >= 0.05:
        print("R$ 0,05")
        return troco(t-0.05)
    elif round(t, 2) >= 0.01:
        print("R$ 0,01")
        return troco(t-0.01)

def main():
    """Função que inicia a máquina."""
    limpaTela()
    VIOLET  = '\033[35m'
    RST     = '\033[00m'
    On_White = '\033[47m'
    print(VIOLET)
    print(18*" ", f"{VIOLET}{On_White}DOCES & CIA - MÁQUINA DE COMPRAS{RST}\n")
    print(24*" ", "''    *****  ''")
    print(24*" ", "    *********")
    print(24*" ", "   ^^^^^^^^^^^")
    print(24*" ", "   \         /")
    print(24*" ", "    \_______/")
    print(VIOLET)
    print("   ", 21*"-", "SEJA BEM-VINDO!", 21*"-")
    print("""    | Aqui na nossa loja vendemos doces caseiros que você vai | 
    | amar!                                                   |
    | Ao escolher, você estará recebendo uma caixa decorada   |
    | e com uma boa quantidade deles! Hmmm... hora de comprar!|""")
    print("   ", 59*"-")
    print(RST)
    _ = input("--> Pressione uma tecla para continuar...")
    menu(5, 5, 5, 5, 5, 0)

main()