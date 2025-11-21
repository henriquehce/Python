"""
Encapsulamento e uso de @property em Python.
"""

class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self._saldo = saldo
        self.__token = "secreto"  # atributo privado

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo.")
        self._saldo = valor


if __name__ == "__main__":
    c = Conta("123", -100)
    print("Saldo:", c.saldo)
    c.saldo = 0
    print("Novo saldo:", c.saldo)
