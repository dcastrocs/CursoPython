num = (int(input('Digite o 1º numero: ')),int(input('Digite o 2º numero: ')),
       int(input('Digite o 3º numero: ')),int(input('Digite o 4º numero: ')))
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
       print(f'O numero 3 esta na posição {num.index(3)+1}')
else:
       print('O valor 3 não foi digitado')
for n in num:
       if n % 2 == 0:
              print(f'Os numeros pares são {n}')
