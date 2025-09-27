from random import randint

print("-="*15+'-')
print('PAR OU IMPAR'.center(25))
print("-="*15+'-')

win = 0

while True:
    num_jo = int(input("Diga um valor: "))

    while True:
        pa_ou_im = input('PAR ou IMPAR? [P/I] ').strip().upper()
        if pa_ou_im not in('PI'):
            print('Apenas P ou I !')
        else:
            break
        print('-'*30)

    comp = randint(0,10)

    tot = comp + num_jo

    print('-' * 16)
    print(f'Você jogou {num_jo} e o computador {comp}.', end=' ')

    if tot % 2 == 0:
        res_j = 'P'
        print(f'Total de {tot} DEU PAR!')
    else:
        res_j = 'I'
        print(f'Total de {tot} DEU IMPAR!')

    print('-' * 30)

    if pa_ou_im == res_j:
        print('Você GANHOU!')
        print("Joguemos novamente..")
        win += 1
        print('-'*30)
        continue
    else:
        print('Você PERDEU!')
        print("-=" * 15 + '-')
        break

print('FIM DE JOGO!', end=' ')
if win == 0:
    print('Ganhou nenhuma vez!')
else:
    print(f"Você ganhou {win} vezes!")