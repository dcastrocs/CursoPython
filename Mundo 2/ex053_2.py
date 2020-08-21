frase = str(input('Digite uma frase: ')).strip().upper() # strip retirou os espaços ante e depois e o upper deixa tudo maiusculo
palavras = frase.split() # Aqui a frase digititada foi separada pelo os espaços entra a frase
junto = ''.join(palavras)# Aqui a palavra é unida sem espaços
inverso = junto[::-1]
print(' O inverso de {} é {} '.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
