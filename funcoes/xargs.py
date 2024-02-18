'''
def sum_until_200(numero):
    resultado = 0
    while resultado < 200:
        resultado += numero
    return resultado


numero = int(input('Digite um valor inteiro: '))
total = sum_until_200(numero)
print("A soma dos números atingiu ou ultrapassou 200. A soma final é:", total)
'''


def soma(*valores):
    resposta = 0
    for num in valores:
        resposta += num
    return resposta


x = soma(1, 2, 3, 4, 5, 6, 7, 8)
print(f'Resultado da soma dos numeros dados foi igual a: {x}')


def somador(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


resultado = 0
while resultado < 200:
    try:
        numero = float(input('Digite um valor inteiro: '))
        resultado = somador(resultado, numero)
        print("Soma parcial:", resultado)
    except ValueError:
        print("Por favor, digite apenas valores.")

print("A soma dos números ultrapassou 200. A soma final é:", resultado)
