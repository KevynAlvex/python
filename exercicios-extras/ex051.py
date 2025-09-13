def cabeca():
    print('Mercadinho do José'.center(30,'='))

def produtos():
    v_tot = 0
    c = 1
    while c <= 8:
        preco = float(input(f'Insira o preço do produto nº{c}: R$'))
        if c == 1:
            menor = preco
            maior = preco
        else:
            if preco > maior:
                maior = preco
            if preco < menor:
                menor = preco

        v_tot+=preco

        c+=1

    print('='*30)
    print(f'Valor total: R${v_tot:.2f}\nMenor valor: R${menor:.2f}\nMaior valor: R${maior:.2f}')

cabeca()
produtos()