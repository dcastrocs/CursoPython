n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
if media <= 5.0:
    print('Aluno(a) Reprovado(a) media final {}' .format(media))
elif media >= 5.1 and media <= 6.9:
    print('Aluno(a)Recuperação media {}' .format(media))
else:
    print('Aluno(a) Aprovado(a)! com a media {}' .format(media))
