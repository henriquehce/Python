aluno = {'nome': '<NAME>',
         'idade': 12, 'Nota_final': 'A',
         'Media': 100.0,
         'Aprovado': True,
         'Matérias':['física', 'Matemárica','Ciências']
         }
aluno.update({'nome': 'Henrique', 'idade': 20})
aluno.update({'endereco': '1926 n236', 'cidade': 'Brasil'})
del aluno['cidade']
print()


for keys, values in aluno.items():
    print(keys, values)
print()
print(aluno.keys())
print(aluno.values())
print(aluno.items())
