import datetime
nascimento = int(input('Informe seu ano de nascimento: '))
ano = datetime.datetime.today().year
idade = ano - nascimento
if idade <= 9:
    print('Sua Idade é {} anos e sua categoria é a Mirim.' .format(idade))
elif idade >=10 and idade <=13:
    print('Sua idade é {} anos e sua Categoria é a Infantil' .format(idade))
elif idade >= 14 and idade <=19:
    print('Sua idade é {} anos e sua categoria sera a Junior' .format(idade))
elif idade == 20:
    print('Sua idade é {} anos e sua categoria sera a Sênior'.format(idade))
else:
    print('Sua idade é {} anos e sua categoria sera a Master'.format(idade))
