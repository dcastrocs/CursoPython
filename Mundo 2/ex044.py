print('1 - Pagamento à vista -- Dinheiro/Cheque ')
print('2 - Pagamento à vista -- Cartão de debito')
print('3 - Pagamento em 2x no cartão de credito')
print('4 - pagamento em 3x ou mais parcelas no cartão de credito')
custo = float(input('Digite o valor da compra: R$'))
pag = int(input('Selecione a forma de pagamento.'))
if pag == 1:
    print('Valor da compra R${:.2f} com 10% de desconto o valor a ser pago será R${:.2f}'.format(custo, custo - (custo * 10 / 100)))
elif pag == 2:
    print('Valor da compra R${:.2f} com 5% de desconto o valor a ser pago será R${:.2f}' .format(custo, custo - (custo * 5 / 100)))
elif pag == 3:
    print('O valor da compra é R${:.2f} parcelado em 2x de {:.2f}' .format(custo, custo / 2))
else:
    print('O valor da compra é R${:.2f} parcelado em 3x ou mais com juros de 20%, o valor total da compra será R${:.2f}' .format(custo, custo + (custo * 20 / 100)))
