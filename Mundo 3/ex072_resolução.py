cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis',
        'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    núm = int(input('Digite um numero entre 0 e 20: '))
    if 0<= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o numero {cont[núm]}')
