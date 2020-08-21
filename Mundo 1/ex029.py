velo = int(input('Digite sua velocidade atual: '))
limite = 80
multa = 7
if velo > 80:
    print('Você ultrapassou o limite de velocidade e foi multado.')
    print('Calculando sua multa....')
else:
    print('Continue respeitando as leis de transito.')
diferença = velo - limite
if diferença > 0:
    total = diferença * 7
    print('O valor da sua multa sera: R${:.2f}' .format(total))
