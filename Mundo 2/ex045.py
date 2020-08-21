from time import  sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0 , 2)
print('''Suas opções
[ 0 ] Pedra
[ 1 } Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('*-' * 11)
print('Computador jogou {}' .format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('*-' * 11)
if computador == 0: #Computador PEDRA
    if jogador == 0:
        print('Empate !')
    elif jogador == 1:
        print('Você Ganhou !')
    elif jogador == 2:
        print('Computador Ganhou!')
    else:
        print('Opção Invalida')
if computador == 1: # Computador Jogou PAPEL
    if jogador == 0:
        print('Computador Ganhou !')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Você GANHOU!')
    else:
        print('Opção INVALIDA!')
if computador == 2: # Computador Jogou Tesoura
    if jogador == 0:
        print('Você Ganhou')
    elif jogador == 1:
        print('Computador Ganhou')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')
