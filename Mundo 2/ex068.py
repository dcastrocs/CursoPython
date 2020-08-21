from random import randint
perdeu = True
c = 0
while perdeu:
    print('=-' * 10)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 10)
    n = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    pc = randint(0, 10)
    soma = n + pc
    res = soma % 2
    escolha = True
    if res == 0 and pi == 'P':
        c += 1
        print('-' * 10)
        print(f'Você Jogou {n} e o computador {pc}. Total de {soma} deu PAR')
        print('-' * 10)
        print('Você Venceu! ')
        print('Vamos jogar novamente....')
    elif res != 0 and pi == 'I':
        c += 1
        print('-' * 10)
        print(f'Você Jogou {n} e o computador {pc}. Total de {soma} deu IMPAR')
        print('-' * 10)
        print('Você Venceu! ')
        print('Vamos jogar novamente....')
    elif res == 0 and pi == 'I':
        print(f'Você Jogou {n} e o computador {pc}. Total de {soma} deu PAR')
        print('Você PERDEU!')
        print('=-' * 10)
        perdeu = False
    elif res != 0 and pi == 'P':
        print(f'Você Jogou {n} e o computador {pc}. Total de {soma} deu IMPAR')
        print('Você Perdeu!')
        print('=-' * 10)
        perdeu = False
print(f'GAME OVER! Você venceu {c} vezes.')
