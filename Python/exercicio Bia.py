from re import S
from this import s


seq = ["sopa","cachorro","salada","gato","otimo"]
a = list(filter(lambda word:word[0]=="g", seq))

print(a)