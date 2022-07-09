a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero:"))

if a%2 == 0 and b%2 == 0:
    print(a + b)
elif a%2 == 0 and b%2 != 0:
    print(a)
elif a != 0 and b%2 == 0:
    print(b)
else:
    print("0")
