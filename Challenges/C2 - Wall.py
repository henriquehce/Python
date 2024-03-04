
rendimento_lata = float(input("Digite o rendimento da lata de tinta: "))
largura_parede = float(input("Digite o largura da parede: "))
altura_parede = float(input("Digite a altura da parede: "))
area = largura_parede *altura_parede
qntd_latas = area / rendimento_lata
print(f'São necessárias {qntd_latas} de tinta para pintar {area} de parede')