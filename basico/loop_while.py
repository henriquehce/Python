valor = 100

while valor >= 0 :
    print(f'{valor} reais')
    valor -= 20
    if valor == 0 :
        print('zerado de dinheiro')
        break