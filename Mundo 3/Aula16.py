lanche = ('hamburgue', 'suco', 'pizza', 'pudim') # tupla não pode ser alterada depois
print(lanche)
print('-=' *30)
for comida in lanche:                                               #Simples sem posição
    print(f'Eu vou comer {comida}')
print('-=' *30)
print(len(lanche)) #conta os itens da tupla
print('-=' *30)
for cont in range(0, len(lanche)):                                  #Mostra a posição
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba')
print('-=' *30)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('-=' *30)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


print('-=' *30)
print(sorted(lanche))                                              # Mostra em ordem
print('-=' *30)
a = (2, 5, 4) #tupla 1
b = (5, 8, 1, 2) #tupla 2
c = b + a # junta as tuplas na ordem que juntei
print(c)
print(c.count(5)) #conta quantas vezes o numero 5 vai aparecer nas tuplas
print(c.index(8)) # mostra em que posição esta o numero 8 na minha tupla
pessoa = ('Diogo', 'vanessa')
del pessoa #Apaga a tupla por completo
