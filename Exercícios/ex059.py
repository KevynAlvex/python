def cabeca():
    print('''    [ 1 ] Somar        [ 4 ] Novo Números
    [ 2 ] Multiplicar  [ 5 ] Sair do Programa
    [ 3 ] Maior''')

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    cabeca()
    opcao = int(input('>> Sua opção: '))
    match opcao:
        case 1:
            print(f'A soma entre {num1} e {num2} é {num1 + num2}')
            print('-=' * 25, '-')
        case 2:
            print(f'O produto entre {num1} e {num2} é {num1 * num2}')
            print('-=' * 25, '-')
        case 3:
            if num1 == num2:
                print('Ambos número são iguais!\nPortanto não tem maior ou menor!')
            else:
                if num1 > num2:
                    maior = num1
                else:
                    maior = num2
                print(f'Entre {num1} e {num2} o maior é {maior} ')
            print('-=' * 25, '-')
        case 4:
            num1 = int(input('Primeiro valor: '))
            num2 = int(input('Segundo valor: '))
        case 5:
            print('-=' * 25, '-')
            pass
        case _:
            print('Opção inválida!')
            print('-=' * 25, '-')