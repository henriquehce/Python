funcionarios = ['Henrique', 'Maria', 'Roberto', 'João', 'Marcela', 'Ronaldo']
turno_dia = ['Henrique', 'Maria', 'Ronaldo']
turno_noite = ['Roberto', 'Marcela', 'João']
tem_carro = ['Henrique', 'João', 'Marcela', 'Ronaldo']

lista3 = []
lista4 = []
lista5 = []
for funcionario in funcionarios:
    if funcionario in turno_dia and funcionario in tem_carro:
        lista3.append(funcionario)
    if funcionario in turno_noite and funcionario in tem_carro:
        lista4.append(funcionario)
    if funcionario not in tem_carro:
        lista5.append(funcionario)

print(f'Funcionários que trabalham de dia e possuem carros: {lista3}')
print(f'Funcionarios que trabalham a noite e possuem carros: {lista4}')
print(f'Funcionarios que não possuem carro: {lista5}')

#-----------------------------------------------------------------------------
list1 = set(tem_carro).intersection(turno_dia)
print(list1)

list2 = set(turno_noite).intersection(tem_carro)
print(list2)

list3 = set(funcionarios).difference(tem_carro)
print(list3)