import time

from colorama import Fore #importando cores
from time import sleep #importando sleep

velocidade_atual = int(input('Qual a velocidade atual do seu carro? '))

if velocidade_atual > 80:
    print(Fore.RED + 'MULTADO! Você ultrapassou o limite permitido de 80km/h!')
    print(Fore.MAGENTA + 'Calculando multa...')
    time.sleep(2)
    #Calculando multa
    multa = (float(velocidade_atual) - 80.0) * 7.0
    print(Fore.RED + 'Você deverá pagar uma multa de ' + Fore.GREEN + f'R${multa:.2f}')
    print(Fore.LIGHTYELLOW_EX + 'Tome cuidado na próxima!')
else:
    print(Fore.CYAN + 'Tenha um bom dia! E sempre dirija com cuidado!')

