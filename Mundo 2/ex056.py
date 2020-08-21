somaidade = 0
mediaidade = 0
maiorIdadeHomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print('___________{}º Pessoa__________'.format(p))
    Nome = str(input('Nome: ')).strip()
    Idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += Idade
    if p == 1 and Sexo in 'Mm':
        maiorIdadeHomem = Idade
        nomevelho = Nome
    if Sexo in 'Mn' and Idade <20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomevelho))
print(' Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
