from random import randint

numeros = (randint(0,10), randint(0,10), randint(0,10),
           randint(0,10), randint(0,10))

print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(n, end=' ')
'''
maior = 0
menor = 0
for pos, n in enumerate(numeros):
    if pos == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if menor > n:
            menor = n

print(f'\nO maior valor foi {maior}\nO menor valor foi {menor}')
'''

print(f'\nO maior valor foi {max(numeros)}\nO menor valor foi {min(numeros)}')