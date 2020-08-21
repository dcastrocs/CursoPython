
n = [2, 5, 9, 1]
print(n)
n[2] = 3
print(n)
n.append(7)
print(n)
n.sort()
print(n)
n.sort(reverse=True)
print(n)
n.insert(1, 8)
print(n)
n.pop()
print(n)
n.pop(2)
print(n)
n.remove(7)
print(n)
if 4 in n:
    n.remove(4)
else:
    print("Não achei o numero 4")

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')
for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('\nCheguei ao final da lista.')

valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('\nCheguei ao final da lista.')

print('Ligação da lista')
a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('=' * 10)

print('Criar a copia da lista')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('=' * 10)