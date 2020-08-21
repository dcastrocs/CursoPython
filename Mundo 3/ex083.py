'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
expressão = str(input('Digite sua expressão: '))
pilha = []
for simb in expressão:
    if simb == '(':
        pilha.append('(') #Adicionou uma ( a lista pilha
    elif simb == ')'
        if len(pilha) > 0: #Verifica se a pilha esta vazia
            pilha.pop() #Remove o ultimo elemento
        else:
            pilha.append(')') # adicionou um ) na pilha
            break
if len(pilha) == 0: # Se a pilha esta vazia
    print('Sua expressão esta valida.')
else: # Se a pilha não estiver vazia
    print('Sua expressão não esta errada.')