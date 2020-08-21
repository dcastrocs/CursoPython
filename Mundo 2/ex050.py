soma = 0
for u in range(1, 7):
    n = int(input('Digite um numero: '))
    soma = soma + n
if n % 2 == 0:
    print('Numeros pares somados: {}'.format(soma))
else:
    print('Nenhum numero digitado é par.')
