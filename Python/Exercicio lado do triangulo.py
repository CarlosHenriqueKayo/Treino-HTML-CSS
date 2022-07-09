a = float(input("Digite o valor do primeiro lado: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))

if a < b + c and b < a + c and c < b + a:
    print("Sim")
if a > b + c or b > a + c or c > a + b:
    print("Nao")
    