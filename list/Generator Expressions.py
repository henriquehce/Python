from sys import getsizeof

numeros = [x * 10 for x in range(10000000)]
print(type(numeros))
print(getsizeof(numeros))

numeros2 = (x * 10 for x in range(10000000))
print(type(numeros2))
print(getsizeof(numeros2))
#nao armazena na memoria
