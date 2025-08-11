def cabeca():
    print('='*35)
    print('ESCOLA MIRANDA'.center(30))
    print('='*35)

cabeca()
nome = input('Nome do Aluno: ').strip()
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('='*35)
if 7 >= media >= 5:
    print(f'O aluno {nome} está na média')
elif media > 7:
    print(f'o aluno {nome} teve um bom aproveitamento!')
else:
    print(f'O aluno {nome} não está na média')
print('='*35)