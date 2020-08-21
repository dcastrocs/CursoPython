lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer Continuar? [S/N]' )).strip().upper()
    if resp in 'N':
        break
print(f'Vode digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao foi encontrado na lista!')