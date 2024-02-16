
#imprimir em sequencia, etc
'''
#imprimindo pra cima
for numero in range(5): 
    print(numero)
print()
#imprimindo negativo
x = 10
for x in range(0,-5,-1): 
    print(x)    

#imprimindo de 2 em 2
print()
for y in range(0,10,2):
    print(y)
------------------------------------------------------------
#imprimindo strings

palavra = 'Banana'

for letra in palavra:
    print(f'{letra} é uma letra da {palavra}')
-----------------------------------------------------------
compra_confirmada = True
dados_da_compra = 'Compra no valor de R$20.0 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada: 
        print(dados_da_compra)
        print('Detalhes enviados para o seu E-mail')
        break
else: print('falha na compra')
--------------------------------------------------------------
#nested loop

for numero1 in range(0,11):
    for numero2 in range(numero1):
        if numero1 % 2 == 0 :
            print(str(numero1) + ' é par')
            break
        else: 
            print(str(numero1) + ' é impar')
            break
--------------------------------------------        
'''
for numero1 in range(0,11):
    print(numero1, end= ' ')
