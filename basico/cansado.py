flexoes = 10
contador = 0
while flexoes > 0:
    contador += 1
    print('flexao numero:', contador)
    if contador > 10:
        print('estou cansado')
        break
print()
flexoes2 = 10

for contador in range(1, flexoes2 + 1):
    print('flexao numero:', contador)
    if contador >= 10:
        print('estou cansado')
        break