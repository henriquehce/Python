'''
Mostrar através do Print, a seguinte frase com certa qntd de variáveis escolhidas

"Pessoa, de I anos, esta tentando aprender python no mês de fevereiro de 2024, e descobriu como são feitas algumas multiplicações, como por exemplo 1101 * 0101, cujo resultado é:

'''
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
matéria = 'python'
data = 'Fevereiro de 2024'
x = 1101
y = 101
mult = (x * y)
resultado = str(mult) #possível opção ao final da frase

print(nome + ", de idade " + idade + ", esta tentando aprender " + matéria + " no mês de " + data + " e descobriu como são feitas algumas multiplicações, como por exemplo 1101 * 0101 cujo resultado é " + str(mult)) #ou resultado

print("\n", mult * 2)