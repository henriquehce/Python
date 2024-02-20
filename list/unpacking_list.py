produtos = ['arroz', 'banana', 'cherry', 'manga', 'maçã']
#               0       1          2
item1, *outros, item3, item4 = produtos
# 0      1      2
print(produtos)
print()
print(item4)
print()
print(outros)
print()
print(outros[0])