num1 = int(input("Digite o primeiro Nota: "))
num2 = int(input("Digite o Segundo Nota: "))
num3 = int(input("Digite o Terceira Nota: "))
s = num1 + num2 + num3 
media = (s / 3)

print(f"A média é: {media:.1f}")

if media >=  5:
    print('aprovado')
else: 
    print('reprovado')