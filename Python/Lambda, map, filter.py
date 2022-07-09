def quadrado(var) : return var**2
quadrado(2)

print(quadrado(2))

seq = [1,2,3]
map(quadrado, seq)
list(map(lambda x:x**2, seq))

list(filter(lambda item:item%2==0, seq))

print(list(filter(lambda item:item%2 ==1, seq)))

str = "Hi guys"
type(str)
print(type)

list = [1, 2, 3]
first = list.pop(0)
print(list)
