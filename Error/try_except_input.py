try:
    num = int(input('Enter a number: '))
    print(f'{num} foi o numero digitado')
except:
    print('Invalid')
finally:
    print('Goodbye')
