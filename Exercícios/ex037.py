def binario(numero):
    num_binario = ''
    numero = numero
    while numero > 0:
        num_binario = str(numero % 2) + num_binario
        numero //= 2

    return f'em binário {num_binario}!'

def octal(numero):
    num_octal = ''
    numero = numero
    while numero > 0:
        num_octal = str(numero%8) + num_octal
        numero //= 8

    return f'em octal {num_octal}!'

def hexadecimal(numero):
    num_hexa = ''
    while numero > 0:
        if numero % 16 <= 9:
            num_hexa = str(numero % 16) + num_hexa
        if numero %16 > 9:
            if numero %16 == 10:
                num_hexa = 'A'+num_hexa
            elif numero %16 == 11:
                num_hexa = 'B'+num_hexa
            elif numero %16 == 12:
                num_hexa = 'C'+num_hexa
            elif numero %16 == 13:
                num_hexa = 'D'+num_hexa
            elif numero %16 == 14:
                num_hexa = 'E'+num_hexa
            elif numero %16 == 15:
                num_hexa = 'F'+num_hexa
        numero //= 16

    return f'em decimal {num_hexa}!'

def cabecalho():
    print('='*35)
    print('TRANSFORMADOR DE BASES'.center(35))
    print('='*35)
    print('''[ 1 ] - BINARIO
[ 2 ] - OCTAL
[ 3 ] - HEXADECIMAL''')
    c = 1
    while c == 1:
        opcao = int(input('Sua escolha:'+'\n'))
        if opcao == 1 or opcao == 2 or opcao == 3:
            c -= 1
        else:
            print('Escolha alguma opção acima!')
    print('='*35)
    return opcao

a = int(input('Digite um número: '))
numero = cabecalho()
if numero == 1:
    print(f'O número {numero} {binario(a)}')
elif numero == 2:
    print(f'O número {numero} {octal(a)}')
else:
    print(f'O número {numero} {hexadecimal(a)}')