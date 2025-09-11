def cabeca():
    print("GRAU'S LOJA".center(30, '='))

def pagamentos():
    tipo = []
    print('='*30)
    formas = ('[1] à vista dinheiro/cheque',
              '[2] à vista cartão',
              '[3] 2x no cartão',
              '[4] 3x ou mais no cartão')
    for i in formas:
        print(i)
    print('='*30)
    while True:
        opcao = int(input('Qual opção? '))
        if opcao not in(1,2,3,4):
            print('Insira apenas um dos valores acima!')
        else:
            tipo.append(opcao)
            break
    if opcao == 4:
        parcelas = int(input('Em quantas parcelas? '))
        tipo.append(parcelas)

    return tipo

def descontos(valor, opcao):
    match opcao[0] :
        case 1:
            valor *= 0.9
        case 2:
            valor *= 0.95
        case 3:
            pass
        case 4:
            valor *= 1.20
        case _:
            print('Valor inválido')

    return valor

def __print__(valor, descontos, opcao):
    match opcao[0]:
        case 1 | 2:
            print(f'Sua compra de R${valor:.2f} vai custar R${descontos:.2f} no final!')
        case 3:
            print(f'Sua compra ficará R${valor:.2f}.')
        case 4:
            print(f"Sua compra será parcelada em {opcao[1]}x de R${descontos/int(opcao[1]):.2f} COM JUROS")
            print(f"Sua compra ficará no total de R${descontos:.2f}!")


cabeca()
valor = float(input('Insira o valor das compras: R$'))
opcao = pagamentos()
valor_final = descontos(valor, opcao)
__print__(valor, valor_final, opcao)
