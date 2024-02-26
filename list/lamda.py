'''
def somar(x):
    return x + 10

print(somar(2))
--------
somar = lambda x, y: x + y + 20
print(somar(2,2))
--------------


def somar(x):
    return x + 10

print(somar(2))

'''
lista1 = [1,2,3,4]

print(list(map(lambda x: x * 2, lista1)))