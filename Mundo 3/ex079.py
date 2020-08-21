num = list()
while True:
    n = (int(input("digite um valor: ")))
    num.append(n)
    c = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if c == 'N':
        break
num.sort()
print(f'Os valores digitados em ordem crescente foram {num}')
