"""
Herança simples e uso de super().
"""

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico...")


class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Au au!")


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def info(self):
        return f"Nome: {self.nome}, Salário: {self.salario}"


class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def info(self):
        return super().info() + f", Setor: {self.setor}"


if __name__ == "__main__":
    c = Cachorro("Rex")
    c.emitir_som()

    g = Gerente("Carla", 5000, "TI")
    print(g.info())
