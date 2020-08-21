maiores = homens = mulheres = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Digite sua Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    prosseguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sexo == 'M' and idade > 17:
        maiores += 1
        homens += 1
    if idade <= 20 and sexo == 'F':
        mulheres += 1
    if sexo == 'F' and idade > 17:
        maiores += 1
    if prosseguir == 'N':
        break
print('=' * 15)
print('FIM DO PROGRAMA')
print('=' * 15)
print(f'Total de pessoas com mais de 18 anos: {maiores} ')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
