# criar uma classe
class Funcionarios:
    pass


# criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# criar parâmentros
usuario1.nome = 'Henrique'
usuario1.sobrenome = 'Cipriani'
usuario1.email = '<EMAIL>'

usuario2.nome = 'Piet'
usuario2.sobrenome = 'ra'
usuario2.email = '<EMAIL>'

print(usuario1.__dict__)
print(usuario2.email)