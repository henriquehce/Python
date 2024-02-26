fruits = ['apple', 'banana', 'pear', 'orange', 'pineapple', 'grapes']
# frutas2 = []

'''
for itens in fruits:
    if 'p' in itens:
        frutas2.append(itens)
'''

#expressao for itens in itens

frutas2 = [itens for itens in fruits if 'a' in itens]
print(frutas2)

valores = [x * 10 for x in range(6)]
print(valores)