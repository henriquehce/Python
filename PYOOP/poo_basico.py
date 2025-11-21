"""
POO Básico – classes, objetos, atributos e métodos.
"""

class Pessoa:
    especie = "Humano"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


if __name__ == "__main__":
    p1 = Pessoa("Ana", 20)
    p2 = Pessoa("João", 25)
    p1.apresentar()
    p2.apresentar()
    print(Pessoa.especie)
