"""
Herança múltipla e herança multinível.
"""

class Logavel:
    def logar(self, msg):
        print(f"[LOG] {msg}")


class Autenticavel:
    def autenticar(self, senha):
        return senha == "1234"


class Usuario(Logavel, Autenticavel):
    def __init__(self, nome):
        self.nome = nome


# Herança multinível
class SerVivo:
    def respirar(self):
        print("Respirando...")


class Animal(SerVivo):
    def mover(self):
        print("Movendo-se...")


class Cachorro(Animal):
    def latir(self):
        print("Au au!")


if __name__ == "__main__":
    u = Usuario("Henrique")
    u.logar("Usuário criado")
    print("Autenticado:", u.autenticar("1234"))

    d = Cachorro()
    d.respirar()
    d.mover()
    d.latir()
