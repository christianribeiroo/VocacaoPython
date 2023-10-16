import time

print('3,2,1...')
time.sleep(3)

print("Bem vindo a calculadora do Chris!")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("escolha a operação: +, -, *, /: ")

if(op == '+'):
    print(f"O resultado da soma  é {n1 + n2}")
if(op == '-'):
    print(f"O resultado da subtração é {n1 - n2}")
if(op == '*'):
    print(f"O resultado da multiplicação é {n1 * n2}")
if(op == '/'):
    print(f"O resultado da divisão é {n1 / n2}")




    







