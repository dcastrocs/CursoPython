listagem = ('Fonte ATX 80 Plus', 500.00,
            'Processador I5', 1400.00,
            'Placa Mãe', 900.00,
            'Memoria DDR4', 1000.00,
            'Placa de Video', 2100.00,)
print('-=' * 20)
print('LISTA DE PREÇO DO COMPUTADOR')
print('-=' * 20)
for i in range(0, len(listagem)):
    if i % 2 ==0:
        print(f'{listagem[i]:.<30}',end='')
    else:
        print(f'R$ {listagem[i]:>7.2f}')
print('-=' * 20)
