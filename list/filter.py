valores = [10, 22, 32, 54, 60, 17]

'''def remover20(x):
    return x > 20


print(list(filter(remover20, valores)))
'''

print(list(filter(lambda x: x > 20, valores)))
