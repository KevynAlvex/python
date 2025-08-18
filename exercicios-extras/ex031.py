from random import randint
from time import sleep

def cabeca():
    print('+-'*10 + '+')
    print('JOKENPO'.center(22))
    print('+-' * 10 + '+')
    #Cabeçalho

def opcoes_loop():
    print('[1] - Pedra\n[2] - Papel\n[3] - Tesoura')
    #Opções print

def dormir():
    print('O computador está escolhendo agora', end='')
    for i in range(0, 3):
        sleep(0.25)
        print('.', end='')
    print('.')

def resultado(player, computador, opcoes):
    print('+-'*10 + '+')
    print(f'O jogador escolheu {opcoes[player]}')
    print(f'O computador escolheu {opcoes[computador]}')
    print(f'Então', end=' ')
    #Decidindo quem ganhou
    if (player == 0 and computador == 2) or (player == 1 and computador == 0) or (player == 2 and computador == 1):
        print('O jogador Ganhou!')
    elif player == computador:
        print('houve um EMPATE!')
    else:
        print('O Computador Ganhou!')


    print('+-' * 10 + '+')

control_game = True # <- Variável de looping p/ controle

while control_game == True:
    cabeca()
    opcoes_loop()
    control_choice = True # <- Looping p/ escolher uma das 3 opções

    opcoes = ('Pedra', 'Papel', 'Tesoura')

    #Loop p/ que o jogador escolha uma opção existente
    while control_choice == True:
        player = int(input('Qual opção você escolhe? '))
        match player:
            case 1:
                player = 0
                control_choice = False
            case 2:
                player = 1
                control_choice = False
            case 3:
                player = 2
                control_choice = False
            case _:
                print('Escolha apenas uma das 3 opções')

    #print para dar uma "visualização" melhor
    dormir()

    # Computador escolhendo sua opção
    computador = randint(0, 2)

    resultado(player, computador, opcoes)

    cont = True
    while cont == True:
        c = input('Gostaria de jogar novamente [S/N]?  '.strip().upper())
        if c == 'N':
            control_game = False
            cont = False
        if c == 'S':
            cont = False
            continue


