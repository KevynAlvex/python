from random import randint

def numero():
    num = randint(0,10)
    return num

print('JOGO DA ADIVINHAÇÃO'.center(30,'='))
print('Gerei um número aleatório de 0 a 10!\nAdivinhe se for capaz!!!')

num_pc = numero()
tentativas = 0

while True:
    player = int(input('Seu palpite: '))
    if player == num_pc:
        tentativas +=1
        if tentativas == 1:
            print('ACERTOU DE PRIMEIRA! Parabéns!')
        else:
            print(f'Acertou em {tentativas} tentativas!')
        break
    else:
        tentativas+=1
        if player > num_pc:
            print('Menos! Tente novamente!')
        else:
            print('Mais! Tente novamente!')