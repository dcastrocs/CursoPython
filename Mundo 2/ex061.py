print('Gerador de Progressão Aritmetica')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
print('-=' * 10)
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo),end='' )
    termo += razão
    cont += 1
print('\n=-=-=-=-=-FIM-=-=-=-=-=-=-=')
