import random

lista = [1,2,3,4,5]
numeros_sorteados = []

for item in lista:
    while True:
        numero = random.choice(lista)
        print("Numero escolhido: " + str(numero))
        if numero not in numeros_sorteados:
            numeros_sorteados.append(numero)
            print(numeros_sorteados)
            break