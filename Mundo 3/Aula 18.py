
teste = list()
teste.append('Diogo')
teste.append(35)
galera = list()
galera.append(teste[:]) # Copia da lista teste
teste[0] = 'Vanessa'    #incluido novo iten na lista
teste[1] = 22           #Incluido novo item na lista
galera.append(teste[:]) #Criado outra copia da lista
print(galera)

print('=-' * 30)
galera2 = [['joao', 19], ['Ana', 33], ['Joaoquim', 13], ['Maria', 45]]
print(galera2)
print(galera2[0])
print(galera2[0][1])
for p in galera2:
    #print(p)
    #print(p[0])
    #print(p[1])
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('=-' * 30)

galera = list() # dados finais
dado = list() # dados temporarios
maior = 0
menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} ´maior de idade.')
        maior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores de idade.')