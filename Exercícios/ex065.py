num = int(input('Insira um número: '))
men = mai = num
cont = 1
soma = num
while True:
    r = input("Quer continuar [S/N] ? ").strip().upper()
    if r not in ('SN'):
        print('Apenas S ou N!')
    else:
        break
while r != 'N':
    num = int(input('Insira um número: '))
    cont +=1
    soma += num
    if num > mai:
        mai = num
    if num < men:
        men = num
    while True:
        r = input("Quer continuar [S/N] ? ").strip().upper()
        if r not in ('SN'):
            print('Apenas S ou N!')
        else:
            break

media = soma/cont

print(f'\nA média entre os {cont} números é {media:.2f}')
print(f'O maior valor é {mai} e o menor é {men}')
