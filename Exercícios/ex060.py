
print('''Para questões de atividade!
Escolha 1 --> O programa fara com WHILE
Escolha 2 --> O programa fara com FOR''')
while True:
    r = int(input('>>> '))
    if r not in (1,2):
        print('Por favor, apenas 1 ou 2!')
    else:
        print('OBRIGADO!\n')
        break

fatorial = 1

num = int(input('Insira um número para calcular o fatorial: '))
print(f'Calculando {num}! ')

if r == 1:
    while num > 1:
        print(f'{num} X', end=' ')
        fatorial *= num
        num-= 1
    print(f'1 = {fatorial}')

if r == 2:
    for i in range(num, 1, -1):
        print(f'{i} X', end=' ')
        fatorial *= i

    print(f'1 = {fatorial}')