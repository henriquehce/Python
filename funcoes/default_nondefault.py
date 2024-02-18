def nome_numero(nome, quantidade):
    print(f'ola {nome}, temos apenas {str(quantidade)} de livros disponiveis')


# primeiro o não default e depois o default
def nome_numero2(nome, quantidade=6):
    print(f'ola {nome}, temos apenas {str(quantidade)} de livros disponiveis')


nome_numero('henrique', 5)
nome_numero2('Maria')
