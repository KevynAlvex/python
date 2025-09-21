from colorama import Fore
q_div = 0
num = int(input('Insira um número: '))
for i in range(1, num+1):
    if num % i == 0:
        print(Fore.GREEN + f'{i}', end=' ')
        q_div +=1
    else:
        print(Fore.RED + f'{i}',end=' ')

if q_div > 2:
    print(Fore.LIGHTWHITE_EX + f'\nO seu número não é PRIMO\nPois pode ser dividido {q_div} vezes!')
else:
    print(Fore.LIGHTWHITE_EX + f'\nO seu número é um número PRIMO')