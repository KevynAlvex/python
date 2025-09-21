'''

EXEMPLO SÓ USANDO JOIN E IF

frase_ori = input().strip().upper().replace(' ', '')
frase_inv = ''.join(reversed(frase_ori))
if frase_inv == frase_ori:
    print('Palindromo')
'''

frase_ori = input().strip().upper().replace(' ', '')
frase_inv = ''
for i in range(len(frase_ori) - 1, -1, -1):
    frase_inv += frase_ori[i]

if frase_ori == frase_inv:
    print('A palavra/Frase é um PALINDROMO')
else:
    print('A palavra/Frase é um NÃO É PALINDROMO')