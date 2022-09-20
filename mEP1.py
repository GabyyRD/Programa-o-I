x = float(input())
op = input()
y = float(input())
if op == "+":
    print(f"{x} + {y} = {x+y}")
elif op == "-":
    print(f"{x} - {y} = {x-y}")
elif op == "*":
    print(f"{x} * {y} = {x*y}")
elif op == "**":
    print(f"{x} ** {y} = {x**y}")
elif op == "//" and y != 0:
    print(f"{x} // {y} = {x//y}")
elif op == "//" and y == 0:
    print("Divisao por 0!")
elif op == "%" and y != 0:
    print(f"{x} % {y} = {x%y}")
elif op == "%" and y == 0:
    print("Divisao por 0!")
else:
    print("Operacao nao reconhecida!")