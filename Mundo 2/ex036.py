casa = float(input('Por favor digite o valor do imavel: R$ '))
salario = float(input('Por Favor informe o valor do seu salario: R$'))
anos = int(input('Quantos anos deseja financiar: '))
meses = anos * 12
parcelas = casa / meses
trinta = salario - (salario * 30 / 100)
if trinta < parcelas:
    print('Infelizmente o valor da parcela supera 30% do seu salario, e impossibilita o financimaneto')
else:
    print('Seu financimento foi aprovado! Salario R${:.2f} numero de parcelas {:.0f} prestação {:.2f}' .format(salario, meses,parcelas))
