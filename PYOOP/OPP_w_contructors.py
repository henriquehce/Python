from datetime import datetime


class Funcionarios:
    def __init__(self, nome, sobrenome, idade, email, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + " " + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.data_nascimento = int(ano_atual - self.data_nascimento)
        return self.data_nascimento


# criar o objeto
usuario1 = Funcionarios('Henrique', 'Cipriani', 18, '<EMAIL>', 2003)

print('idade =', Funcionarios.idade_funcionario(usuario1))
