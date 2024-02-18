valor = int(input('Digite um valor: '))

while valor > 50:
    valor = (valor * 0.1) + valor
    print(f'valor final = R${valor:.2f}')
    break
if valor <=50: print(f'Valor publicado foi de R${valor:.2f}')