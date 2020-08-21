n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('O primeiro numero digitado foi {} e ele é maior que o segundo numero digitado {} '.format(n1, n2))
elif n2 > n1:
    print('O segundo numero digitado foi {} e ele é maior que o primeiro numero digitado {} '.format(n2, n1))
else:
    print('Os numero digitados tem o mesmo valor')
