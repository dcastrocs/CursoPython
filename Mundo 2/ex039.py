import datetime
nascimento = int (input('Digite seu ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - nascimento
maioridade = 18
if idade == maioridade:
    print('Esta na hora de realizar o alistamento militar.')
elif idade > maioridade:
    print('Você ja realizou o alistamento a {} anos atras.'.format(int(idade - maioridade)))
else:
    print('Você ainda precisa esperar {} anos para realizar o alistamento'.format(int(maioridade - idade)))
