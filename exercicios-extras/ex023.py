def cabeca():
    print('='*35)
    print('PROMOÇÃO DE DIA DAS MULHERES!'.center(30))
    print('='*35)

compra = float(input('Qual o valor da sua compra? R$'))
sexo = input('Qual seu sexo [F/M]? ').strip().upper()
if sexo == 'M':
    valor_desc = compra - (compra * 0.05)
    print(f'Valor total da sua compra R${compra:.2f}\nValor com desconto R${valor_desc:.2f}')
elif sexo == 'F':
    valor_desc = compra - (compra * 0.13)
    print(f'Valor total da sua compra R${compra:.2f}\nValor com desconto R${valor_desc:.2f}\nFELIZ DIAS DAS MULHERES')

