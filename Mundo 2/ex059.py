'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
print('==========Menu de opções==========')
print('[ 1 ] Somar')
print('[ 2 ] Multiplicar')
print('[ 3 ] Maior')
print('[ 4 ] Novos Números')
print('[ 5 ] Sair do programa')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
menu = int(input('Digite sua opção: '))
soma = n1 + n2
multi = n1 * n2
sair = False
while not sair:
    if menu == 1:
        print('O valor {} + {} é {}'.format(n1, n2, soma))
        sair = True
    elif menu == 2:
        print('O valor {} x {} é {}'.format(n1, n2, multi))
        sair = True
    elif menu == 3:
        if n1 > n2:
            print('O Valor {} é Maior que {}'.format(n1, n2))
            sair = True
        elif n1 < n2:
            print('O valor {} é maior que {}'.format(n2, n1))
            sair = True
        else:
            print('Os valores de {} e {} são iguais'.format(n1, n2))
            sair = True
    elif menu == 4:
        n1 = int(input('Digite novamente o primeiro valor: '))
        n2 = int(input('Digite o segundo valor novamente: '))
        print(menu)
    elif menu == 5:
        sair = True


print('Fim')
