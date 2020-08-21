
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições: ',end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi {men} nas posições: ',end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...',end='')
print()
#=========================================================================================
valores = [int(input('Digite o valor para a posição {}: '.format(i))) for i in range(5)]
print('=-' * 30)
print('Você digitou os valores {}: '.format(valores))

maior = max(valores)
menor = min(valores)

print('O maior valor digitado foi o {} nas posições '.format(maior), end='')
for ind, val in enumerate(valores):
    if val == maior:
        print(f'{ind}...', end='')

print('\nO menor valor digitado foi o {} nas posições '.format(menor), end='')
for ind, val in enumerate(valores):
    if val == menor:
        print(f'{ind}...', end='')
#===============================================================================================

n = [int(input(f'\nDigite um valor para a posição {pos}: ')) for pos in range(5)]
print(f'\nVocê digitou os valores {n}.')
print(f'\nMaior nº digitado foi {max(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == max(n))}.')
print(f'Menor nº digitado foi {min(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == min(n))}.')