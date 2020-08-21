# from math import sqrt                                             #// Aqui importei somente o modulo sqrt da biblioteca math
# nun = int (input('Digite um numero: '))                           #// Recebe o numero a descobrir a raiz
# nun = sqrt(nun)                                                   #// Aqui calcula a raiz da variavel nun
#print ('A raiz de {} é igual a {}'.format (nun, raiz)              #// exibe a raiz para o usuario.

import math
nun = int (input('Digite um numero: '))
raiz = math.sqrt (nun)
print ('A raiz de {} é igual a {}'.format (nun, raiz))
