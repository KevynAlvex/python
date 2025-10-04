'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))

numeros = (num1,num2,num3,num4)
'''

numeros = (int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')),
           int(input('Digite o quarto número: ')))

print(f'Você digitou os seguintes números: {numeros}')

if numeros.count(9) > 0:
    print(f'O número nove apareceu {numeros.count(9)} vezes')
else:
    print('O número nove não foi digitado!')

if numeros.count(3) == 0:
    print('O número 3 não apareceu!')
    pass
else:
    print(f'O primeiro 3 apareceu na posição {numeros.index(3)+1}')

pares = 0
print('Os números PARES digitados foram:', end=' ')
for n in numeros:
    if n % 2 == 0:
        pares +=1
        print(n, end=' ')

if pares == 0:
    print('Nenhum!')