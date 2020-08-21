pessoas = list()
temp = list()
peso = list()
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Digite seu peso: ')))
    pessoas.append(temp[:])
    peso.append(temp[1])
    temp.clear()
    pros = str(input('Deseja continuar ? [S/N]: ')).strip().upper()
    if pros == 'N':
        break
print(f'Você cadastrou {len(pessoas)} pessoas')
for p in pessoas:
    if p[1] == max(peso):
        print(f'O maior peso foi {max(peso)}KG de {p[0]}')
for p in pessoas:
    if p[1] == min(peso):
        print(f'O menor peso foi {min(peso)}Kg de {p[0]}')
