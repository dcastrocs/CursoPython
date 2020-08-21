# Crie um programa que leia o nome de uma pessoal e diga se ela SILVA no nome. (true ou false) 
nome = str(input('Qual o seu nome completo: ')).strip()
print ('Seu nome tem Silva? {}'.format ('silva' in nome.lower()))
