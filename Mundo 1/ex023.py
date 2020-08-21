#faça um programa que leia um nimero de 0 a 9999 e mostre na tela cada um dos digitos separados. 
#exemplo: digite um numero: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
nun = int (input('Informe um número: '))
u = nun // 1 % 10
d = nun // 10 % 10
c = nun // 100 % 10
m = nun // 1000 % 10
print ('Analisando o numero {}'.format (nun))
print ('Unidade: {}' .format(u))
print ('Dezena: {}' .format(d))
print ('Centena: {}'.format (c))
print ('Milhar: {}'.format(m))
