print('Ola Mundo')
#Repetir o print('Ola Mundo')
for c in range (0,6): # vai repetir 6x se colocar (1, 6) ai ele vai mostrar 5x
    print('Ola Mundo')
print('Saiu do laço')
# __________________________________________________________________
for c in range (1, 6):
    print(c)
print('Neste caso vai do 1 ate o 5')
# __________________________________________________________________
for c in range (0, 6):
    print(c)
print('Neste caso inicia no 0 e vai ate o 6')
# __________________________________________________________________
for c in range (6, 0, -1):
    print(c)
print('Neste caso estamos diminuindo 1 na contagem')
# __________________________________________________________________
# Realizando soma com o for
soma = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    soma = soma + n
print('A soma de todos os valores é: {}'.format(soma))
# ____________________________________________________________________

i = int(input('Digite o inicio da contagem:'))
f = int(input('Digite o fim da contagem: '))
p = int(input('Maneira que ira contar: 1 em 1, 2 em 2, 100 em 100: '))
for c in range(i, f+1 , p):
    print(c)
