'''import random
numeros = [0,1,2,3,4,5]
n = random.choice(numeros)
us = int (input('Digite um numero de 0 a 5 e descubra o numero que o computador gerou, sera que você acerta! '))
if us == n:
    print('Parabens ! você descobriu o numero correto ! Que sorte !')
else:
    print('Você errou!, Computador escolheu {} e você escolheu {}'.format(n, us))
'''
import random
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computador = random.choice(numeros)
usuario = int(input('Digite um numero de 0 a 10 e descubra se você escolheu o mesmo do computador: '))
cont = 0
while usuario != computador:
    if usuario != computador:
        print('Você jogou {} e o computador jogou {} '.format(usuario, computador))
        cont += 1
        usuario = int(input('Tente novamente! Digite um numero entre 0 e 10: '))
        computador = random.choice(numeros)
    else:
        print('Parabens você acertou !')
print('Você Jogou {} vezes e conseguiu ganhar PARABENS!'.format(cont))