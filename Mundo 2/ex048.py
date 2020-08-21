print('--//-' * 10)
print('Neste programa vamos realizar a soma dos numeros de 1 a 500 que são divisiveis por 3')
print('--//-' * 10)
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        cont += 1
print('A soma de todos os {} numero,no total somado será {} '.format(cont, soma))
