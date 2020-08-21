numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero entre 0 e 20: '))
while n not in range(0,21):
    n = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print('Você digitou o numero', end= ' ')
print(numeros[n])

