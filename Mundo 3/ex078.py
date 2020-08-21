valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for pos, n in enumerate(valores):
    print(f'Na posicção {pos} encontrei o valor {n}')
print('-=' * 20)
print(f'Os numeros digitados foram {valores}')
print('-=' * 20)
print(f'O maior valor é {max(valores)} na posição {pos}....')
print('-=' * 20)
print(f'O menor valor é {min(valores)} na posição {pos}....')
print('-=' * 20)
for i, v in valores:
    if v == max(valores):
        print(f'Posição {v}...')
'''
valores.sort()
print(f'Os valores na ordem crescente são {valores}')
print('-=' * 20)
valores.sort(reverse=True)
print(f'Valores na ordem decrescente são {valores}')'''