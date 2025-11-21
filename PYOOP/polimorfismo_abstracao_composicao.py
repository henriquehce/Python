"""
Polimorfismo, classe abstrata e composição.
"""

from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def area(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


# Composição
class Motor:
    def ligar(self):
        print("Motor ligado.")

    def desligar(self):
        print("Motor desligado.")


class Carro:
    def __init__(self):
        self.motor = Motor()  # composição

    def ligar(self):
        self.motor.ligar()

    def desligar(self):
        self.motor.desligar()


if __name__ == "__main__":
    # Polimorfismo
    formas = [Quadrado(3), Retangulo(2, 6)]
    for f in formas:
        print("Área:", f.area())

    # Composição
    c = Carro()
    c.ligar()
    c.desligar()
