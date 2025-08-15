nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1+nota2)/2

if media >= 5 and media <= 6.9:
    print('A nota do aluno foi {:.1f}: RECUPERAÇÃO'.format(media))
elif media >= 7:
    print('A nota do aluno foi {:.1f}: APROVADO'.format(media))
else:
    print('A nota do aluno foi {:.1f}: REPROVADO'.format(media))