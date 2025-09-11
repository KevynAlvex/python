print('='*35)
print('Emprestimos Bancarios'.center(33))
print('='*35)
val_casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar a casa? '))*12
print('='*35)
if (val_casa / anos) > (sal*0.3):
    print('Não será possível fazer o empréstimo, pois a parcela da casa excede 30% do salário!')
    print(f'Parcela: R${val_casa/anos:.2f}\n30% do salário: R${sal*0.3:.2f}')
else:
    print('Empréstimo realizado com sucesso!')
    print(f'Suas parcelas ficaram no valor de R${val_casa/anos:.2f} por {anos} meses')