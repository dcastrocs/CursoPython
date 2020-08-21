nome = str(input('Qual seu nome? '))
if nome == 'Diogo':
    print('Que nome bonito!')
elif nome == 'Roberto' or nome == 'Debora' or nome == 'Vanessa':
    print('Seu nome é bem popular no Brasil. ')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {} !'. format(nome))
