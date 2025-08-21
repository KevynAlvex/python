#print('\033[7;32;41mOlá, mundo!\033[m')

#a = 3
#b = 5
#print(f'Os valores são \033[33;44m{a}\033[m e \033[31;42m{b}\033[m')

nome = 'Kevyn'
cores = {'limpa':'\033[m',
         'amarelo':'\33[33m'}

print(f'Olá, {cores['amarelo']}{nome}{cores['limpa']}')