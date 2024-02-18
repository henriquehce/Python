def soma(numero1, numero2):
    resultado = numero1 + numero2
    print(resultado)


def frase(frase1, frase2):
    frase_completa = frase1 + ' ' + frase2
    print(frase_completa)


def nome_numero(nome, quantidade):
    print(f'ola {nome}, temos apenas {str(quantidade)} de livros disponiveis')


soma(0, 5)
frase('ola', 'henrique')
nome_numero('henrique', 5)
