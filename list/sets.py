

list1= [10,20,30,40,50,60,7,8,9]
list2= [10,20,10,11,12]


num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #union retira os repetidos e junta os 2
print(num1 - num2) #difference
print(num1 ^ num2) #tira os duplicados nas 2 listas
print(num1 & num2) #iguais
print(len(num1))
print()

s1 = {1,2,3,4,5,6,1,2}
s1.add(8)
print(s1)
print()
s1.update({11,12,14})
s1.remove(11)
s1.discard(12)
print(s1)
print()
print(type(s1))
print(type(list1))