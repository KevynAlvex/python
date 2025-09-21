n = int(input('Insira um número para ver sua tabúada: '))
print(f'TABUADA DO {n}'.center(15))
for i in range(0,11):
    print(f'{n} x {i} = {n*i}'.center(15))

print('FIM'.center(15))