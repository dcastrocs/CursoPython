# Faça um programa que leia o nome completo de uma pessoa, mostrando o primeiro nome e o ultimo nome separadamente
# Exemplo: Diogo Vidal de Castro
# Primeiro = Diogo
# Ultimo = Castro
#n = str(input(' Digite seu nome completo: ')).strip
#nome = n.split()
#print('Muito prazer em te conhecer!')
#print('Seu primeiro nome é{}' .format(nome[0]))
#print('Seu ultimo nome é; {}' .format(nome[len(nome)-1]))
nome = str(input('Digite seu nome completo: ')).strip().split()
q = len(nome)-1
print('Seu primeiro nome é: {} '.format(nome[0]))
print('Seu último nome é: {} '.format(nome[q]))
