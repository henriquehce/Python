number_list = []

while True:
    try:
        num = int(input('Enter a number (Digite -1 para finalizar): '))
        number_list.append(num)
        number_list.sort()
    except:
        print('Não são aceitas letras dentro da lista')
        print(f'Lista final foi igual a: {number_list}')
        break
    finally:
        print('Programa finalizado')
