from random import randint
n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
t = (n1, n2, n3, n4, n5)
menor = t[0]
maior = t[0]
if menor > t[1]:
    menor = t[1]
if menor > t[2]:
    menor = t[2]
if menor > t[3]:
    menor = t[3]
if menor > t[4]:
    menor = t[4]
if maior < t[1]:
    maior = t[1]
if maior < t[2]:
    maior = t[2]
if maior < t[3]:
    maior = t[3]
if maior < t[4]:
    maior = t[4]
print('Os Valores sorteados foram {} '.format(t))
print('*-' * 20)
print('O menor valor sorteado foi {}'.format(menor))
print('-=' * 20)
print('O maior valor sorteado foi {}'.format(maior))
print('-=' * 20)