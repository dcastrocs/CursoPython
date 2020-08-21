print('=' * 30)
print('   INFO DRAGON INFORMATICA')
print('=' * 30)
total = 0
cont = 0
menor = 1000000000000000000000000000000000000000000
maior = 0
barato = ''
while True:
    prod = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    total = preço + total
    con = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    if preço > 1000:
        cont += 1
    if preço > maior:
        maior = preço
    if preço < menor:
        menor = preço
        barato = prod

    if con == 'N':
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00 reais')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
'''
O total da compra foi R$ {total}
Temos {} Produtos Custando mais de R$ 1000.00
O produto mais barato foi {} euq custa R$ {}
'''