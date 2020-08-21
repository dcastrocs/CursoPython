import random
n1 = (input('Primeiro aluno: '))
n2 = (input('Segundo aluno: '))
n3 = (input('Terceiro Aluno: '))
n4 = (input('Quarto Aluno: '))
Lista = [n1, n2, n3, n4]
random.shuffle(Lista)
print('A ordem de apresentação sera: ')
print(Lista)
