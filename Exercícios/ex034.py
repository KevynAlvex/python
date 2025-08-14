#pede o salário
sal = float(input('Qual o salário atual do funcionário? R$'))

if sal <= 1250.00:
    #Aumento de 15%
    sal_a = sal*1.15
    #Ou sal_a = sal + (sal * 15 / 100)
else:
    #Aumento de 10%
    sal_a = sal*1.10

print('-'*30)
print(f'O funcionário que recebia R${sal:.2f}, passa a ganhar R${sal_a:.2f}')