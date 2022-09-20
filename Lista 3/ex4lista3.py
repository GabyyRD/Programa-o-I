'''4. Faça o rastreio (teste de mesa) dos programas abaixo. O que cada um imprime?
a) 
def funcao1(arg):
    if arg < 10:
        funcao1(arg + 1)
    else:
        print(arg)

funcao1(0)
Resposta: Imprime o número que foi enviado.

b)
def funcao2(arg):
    print(arg)
    if arg < 10:
        funcao2(arg + 1)
    
funcao2(0)
Resposta: Imprime os números de 0 até 'arg'.

c)
def funcao3(arg):
    if arg < 10:
        funcao3(arg + 1)
    print(arg)

funcao3(0)
Resposta: Imprime os números de 'arg' até 0.'''