def cabeca():
    print('='*35)
    print('ALISTAMENTO MILITAR'.center(30))
    print('='*35)
    print('JÁ SE ALISTOU?')

cabeca()
control = 1
while control == 1:
    alistado = input('[S/N]? ').strip().lower()
    if alistado == 's':
        print('OBRIGADO POR SE ALISTAR!')
        control += 1
    elif alistado == 'n':
        idade = int(input('Quantos anos você tem? '))
        if idade > 18:
            print(f'Você está atrasado {idade - 18} anos para se alistar!\nSe aliste o mais rápido possível!')
        else:
            print(f'Ainda faltam {18 - idade} anos!\nLembre-se de alistar-se no exercito')
        control += 1
    else:
        print('CARACTER INVÁLIDO!')
