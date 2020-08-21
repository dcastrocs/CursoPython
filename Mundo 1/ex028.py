import random
numeros = [0,1,2,3,4,5]
n = random.choice(numeros)
us = int (input('Digite um numero de 0 a 5 e descubra o numero que o computador gerou, sera que você acerta! '))
if us == n:
    print('Parabens ! você descobriu o numero correto ! Que sorte !')
else:
    print('Você errou!, Computador escolheu {} e você escolheu {}'.format(n, us))

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#