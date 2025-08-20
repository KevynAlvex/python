print('EMPRESTIMO BANCÁRIO'.center(35))
valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
print('-'*25)
meses = anos * 12
prestacao = valor_casa / meses

if prestacao > (salario*0.3)