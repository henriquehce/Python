estados = ['RJ', 'SP', 'SC']

numeros = [2, 4, 5, 3.0]
        #  0  1  2  3
       #  -4 -3 -2 -1

print(numeros)
numeros[0] = 1
print(numeros)
numeros.pop(2) #apaga
print(numeros)
numeros.insert(2, 5)
print(numeros)
numeros.insert(1, 7)
numeros.insert(2, 2)
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
numeros.remove(3)
print(numeros)