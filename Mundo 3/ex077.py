palavras = ('beliche', 'borracha', 'cachecol', 'cachimbo',
            'cacho', 'cachorro', 'chá', 'chaleira', 'chao',
            'chapeu', 'chave', 'chicote', 'chinelo', 'chocolate',
            'chuchu', 'chupeta', 'chuva', 'chuveiro', 'concha',
            'ficha', 'galocha', 'machado', 'mancha', 'mochila')
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='  ')
