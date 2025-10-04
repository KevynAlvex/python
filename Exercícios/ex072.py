numeros = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')

cont = 'S'
while cont == 'S':
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 20 >= num >= 0:
            print(f'Você digitou o número {numeros[num]}')
            break
        else:
            print('Apenas números entre 0 e 20!!!')

    cont = input('Quer continuar [S/N] ? ').strip().upper()