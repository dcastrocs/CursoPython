tempo = int (input('Quantos anos tem seu carro ?'))
if tempo <=3:
    print('Seu carro esta novo ')
else:
    print('Carro velho')
print('Fim do programa')

nome = str(input('Qual seu nome ?'))
if nome == 'Diogo':
    print('Que nome maravilhoso')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 6.0:
    print('A sua media foi boa! Parabens !')
else:
    print('A sua media foi ruim! Estude mais !')
