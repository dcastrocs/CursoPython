# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = int(input('Digite a distância da viagem em km: '))
if km <= 200:
    print('O valor da viagem sera: R${:.2f} '.format(km * 0.50))
else:
    print('O valor da sua Viagem sera: R$ {:.2f} '.format(km * 0.45))
