x = float(input("Digite o primeiro numero: "))
y = float(input("Digite o segundo numero: "))
z = input("Digite o sinal")

if z == "+":
    operacao = x + y
elif z == "-":
    operacao = x - y
elif z == "*":
    operacao = x * y
elif z == "/":
    operacao = x / y
else:
    print("Sinal inválido")

print(operacao)



