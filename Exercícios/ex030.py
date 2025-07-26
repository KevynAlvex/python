#fiz com def só para não esquecer
from colorama import Fore #cor da string

def imparoupar(numero): #funcção para calcular par ou impar
    if numero % 2 == 0:
        print(f'O número {numero} é ' + Fore.CYAN + 'PAR')
    else:
        print(f'O número {numero} é ' + Fore.RED + 'ÍMPAR')

num = int(input('Digite um número: '))
imparoupar(num)