from random import randint
from time import sleep

def cabeca():
    print('Suas opções')
    opcoes = ('[1] Pedra',
              '[2] Papel',
              '[3] Tesoura')
    for opcao in opcoes:
        print(opcao)

def player():
    opcao = ''
    while True:
        jogada = int(input('Qual sua jogada? '))
        if jogada not in (1,2,3):
            print('Escola apenas alguma das opções acima!')
        else:
            if jogada == 1:
                opcao += 'PEDRA'
            if jogada == 2:
                opcao += 'PAPEL'
            if jogada == 3:
                opcao += 'TESOURA'
            break
    return opcao

def machine():
    opcao = ''
    jogada = randint(1,3)
    if jogada == 1:
        opcao += 'PEDRA'
    if jogada == 2:
        opcao += 'PAPEL'
    if jogada == 3:
        opcao += 'TESOURA'
    return opcao

def jogo(player,pc):
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    print('-=' * 20 + '-')
    if player == pc:
        print(f'Ambos escolheram {player}, portanto, EMPATE')
    if (player == 'PEDRA' and pc == 'TESOURA') or (player == 'TESOURA' and pc == 'PAPEL') or (player == 'PAPEL' and pc == 'PEDRA'):
        print(f'Jogador --> {player} x {pc} <-- Computador\nO jogador VENCEU!')
    elif (pc == 'PEDRA' and player == 'TESOURA') or (pc == 'TESOURA' and player == 'PAPEL') or (pc == 'PAPEL' and player == 'PEDRA'):
        print(f'Jogador --> {player} x {pc} <-- Computador\nO computador VENCEU!')
    print('-=' * 20 + '-')


cabeca()
jogador = player()
computador = machine()
jogo(jogador,computador)
