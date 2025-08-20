from random import randint
from time import sleep

def cabeca():
    print('+-'*15 + '+')
    print('|' + 'GUESS THE NUMBER!'.center(29) + '|')
    print('+-' * 15 + '+')

def computador(): #função para sortear o número do computador
    num = randint(1, 5)
    return num

def pensar():
    print('O computador está pensando em um número', end='')
    for i in range(0, 3):
        sleep(0.75)
        print('.', end='')
    print('\nO computador pensou, tente adivinhar!')

def comparar(p_y, p_c):
    if p_y == p_c:
        print('Você acertou! Parabéns!')
    else:
        print(f'Você errou infelizmente! O número escolhido pelo computador foi {p_c}')

control_game = True #Var para controlar o loop do jogo
while control_game: #Game loop
    cabeca()
    pensar()
    maquina = computador()
    garant = True
    while garant:         #garantindo que o número sera entre 1 e 5
        player = int(input('Escolha um número entre 1 e 5 \nSeu número: ')) #jogador escolhe o número
        if 1 <= player <= 5:
            garant = False
            continue
        else:
            print('Por favor, apenas números entre 1 e 5!')

    comparar(player, maquina)

    finishi = False #var para controlar se o jogador quer continuar ou não
    decision = input('Gostaria de jogar novamente [s/n]? ').strip().lower()
    while finishi == False: #loop para decidir se continua ou não
        if decision != 's' or 'n':
            print('Digite apenas S ou N')
        if decision == 's':
            finishi = True
        elif decision == 'n':
            finishi = True
            control_game = False
            print('Obrigado por jogar!')

