from array import array

letra = ['a', 'b', 'c', 'd']
numeros_inteiros = [1, 2, 3, 4, 5, 6, 7, 8]
numeros_floats = [1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2]

print(letra)
print(numeros_inteiros)
print(numeros_floats)
print()

letra = array('u', ['a', 'b', 'c', 'd'])
numeros_inteiros = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
numeros_floats = array('f', [1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2 ])
print(letra)
print(numeros_inteiros)
print(numeros_floats)
