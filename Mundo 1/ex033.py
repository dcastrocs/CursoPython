# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
n3 = float(input('Digite o 3º um valor: '))
if n1 > n2 and n1 > n3:
    print('O maior valor é {}' .format(n1))
if n2 > n1 and n2 > n3:
    print ('O maior valor é {} '.format(n2))
if n3 > n1 and n3 >n2:
    print('O maior valor é {} '.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor valor é {}' .format(n1))
if n2 < n1 and n2 < n3:
    print ('O menor valor é {} '.format(n2))
if n3 < n1 and n3 <n2:
    print('O menor valor é {} '.format(n3))
'''
a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
#Verifica o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c >a and c>b:
    maior = c
print('O maior valor é {} '.format(maior))
print('O Menor valor é: {} '.format(menor))

'''