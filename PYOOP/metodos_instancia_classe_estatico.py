"""
Demonstração dos três tipos de métodos:
instância, classe e estático.
"""

class Exemplo:
    contador = 0

    def __init__(self):
        Exemplo.contador += 1

    def metodo_instancia(self):
        print("Método de instância ->", self)

    @classmethod
    def metodo_classe(cls):
        print("Método de classe ->", cls, "| contador:", cls.contador)

    @staticmethod
    def metodo_estatico(a, b):
        return a + b


if __name__ == "__main__":
    e1 = Exemplo()
    e2 = Exemplo()
    e1.metodo_instancia()
    Exemplo.metodo_classe()
    print("Soma estática:", Exemplo.metodo_estatico(10, 20))
