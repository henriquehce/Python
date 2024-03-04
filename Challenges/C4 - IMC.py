altura = float(input("Digite sua altura em centimetros: "))
peso = float(input("Digite seu peso em quilogramas: "))


def calculo_imc(peso, altura):
    imc = peso / (altura/100)**2
    print(f'O seu IMC é igual a {imc}')
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Normal")
    elif 30.0 <= imc <= -34.9:
        print("Obesidade grau 1")
    elif 35.0 <= imc <= -39.9:
        print("Obesidade grau 2")
    elif imc > 40.0:
        print("Obesidade grau 3")

calculo_imc(peso, altura)
