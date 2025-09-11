def media(nota1, nota2):
    media = (nota1 + nota2)/2

    if media < 5.0:
        return f'ESTÁ REPROVADO!'
    elif media > 7.0:
        return f'ESTÁ APROVADO!'
    else:
        return f'ESTÁ DE RECUPERAÇÃO!'

def cabeca():
    print('='*35)
    print('ESCOLA PRISON'.center(35))
    print('=' * 35)

cabeca()
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = media(n1,n2)
print(f'O aluno {media}')