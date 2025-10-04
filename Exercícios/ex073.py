from operator import index

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Botafogo',
         'Bahia', 'Fluminense', 'São Paulo', 'RB Bragantino', 'Grêmio',
         'Corinthians', 'Ceará', 'Vasco DA Gama', 'Atletico-MG', 'Internacional',
         'Santos', 'Juventude', 'Vitória', 'Fortaleza EC', 'Sport Recife')

print('Lista com os times do brasileirão: ')

for pos, time in enumerate(times):
    print(f'{time} -', end=' ')
    if pos in([5,10,15]):
        print()

print()

print('='*50)
print('Os 5 primeiros são: ')
print(times[:5])

print('='*50)
print('Os quatros últimos são: ')
print(times[-4:])

print('='*50)
print('Times em ordem alfabética')
for pos, time in enumerate(sorted(times)):
    print(f'{time} -', end=' ')
    if pos in([5,10,15]):
        print()

print()

print('='*50)
print('O chapecoense está na série B')
print(f'Porém temos o Grêmio na {times.index("Grêmio")+1}ª Posição')