seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = len(list(filter(lambda item:item%2 == 0, seq)))
impar = len(list(filter(lambda item:item%2 != 0, seq)))

print("Quantidade de numero par:", par,"," "Quantidade de numero impar:", impar)