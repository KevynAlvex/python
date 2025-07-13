from random import shuffle
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))
alunos = [a1, a2, a3, a4]
shuffle(alunos)

print('='*20)
print(f'A ordem de apresentação será a seguinte:\n{alunos}')
print('='*20)