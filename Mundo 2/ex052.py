n = int(input('Digite um numero e descubra se ele é primo: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ') #Adiciona cor aos numeros
        total += 1
    else:
        print('\033[31m', end=' ') #Adiciona cor aos numeros
    print('{}'.format(c),end='')
print('\n\033[m O numero  {} foi divisivel {} vezes'.format(n, total))
if total == 2:
    print('E por isso ele pe PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')
