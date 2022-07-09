a = str(input("Digite o planeta: "))
b = int(input("Digite o diametro: "))

print("O diamentro do planeta", a, "é de", b,"kilometros")

planeta = "Terra"
diametro = 12742

a = "O diametro da {0} é de {1} kilometros." 
print (a.format(planeta,diametro))