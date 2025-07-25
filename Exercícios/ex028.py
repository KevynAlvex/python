from random import choice
from time import sleep
numeros = [0, 1, 2, 3, 4, 5] #randint(0, 5)
escolha_pc = choice(numeros)
#Poderia usar a importação randint, seria mais simlples

print('='*40)
print('  C H O I C E  T H E  N U M B E R S')
print('='*40)
escolha_usu = int(input('Escolha um número entre 0 e 5!\nSe acertar você ganha, se não o computador ganha!\nSua escolha: '))
print('processando')
sleep(2)
if escolha_usu == escolha_pc:
    print('\nParabéns, você acertou!')
else:
    print(f'\nInfelizmente você errou!\nO número escolhido pelo computador foi {escolha_pc}')
