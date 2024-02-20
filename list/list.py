user_numbers = input('Enter a number with comma separated: ')

number_list = user_numbers.split(',')
print(number_list)

number_tuple = tuple(number_list)
print(number_tuple) #pode adicionar nada, +é fixo