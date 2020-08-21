salario = float(input('Digite seu salario atual: R$ '))
if salario <= 1250.00:
    print('Seu novo salario será: R${:.2f} '.format(salario * 1.15))
else:
    print('Seu novo salario será de R${:.2f}'.format(salario * 1.10))

'''
salario = float(input('Digite seu salario atual: R$ '))
if salario <= 1250.00:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem Ganhava R$ {:.2f} passa a ganhar R$ {:.2f} Agora.' .format(salario, novo))
