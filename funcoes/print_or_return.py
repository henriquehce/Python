# pega o codigo, joga na tela e descarta
def cliente1(nome):
    print(f'ola {nome}, porém nada foi salvo', end='" "')


# pega o codigo, armazena o valor e fica disponível para usar em outros locais
def cliente2(nome):
    return f'ola {nome} seu nome foi salvo'


x = cliente1('Joao')
y = cliente2('maria')

print(x)
print(y)
