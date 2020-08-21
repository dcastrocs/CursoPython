
while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    for n in (1,2,3,4,5,6,7,8,9,10):
        print('{} x {} = {}'.format(n, tab, tab * n))

print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')