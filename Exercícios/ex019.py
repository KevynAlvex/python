from random import choice

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

aS = choice([a1, a2, a3, a4])

print('='*20)
print(f'O aluno(a) escolhido(a) foi:\n{aS}')
print('='*20)