sal = float(input('Qual o salário do funcionário? R$'))
sal_n = sal + ((sal * 15)/100)
print(f'Um funcionário que ganhava R${sal}, com 15% de aumento, passa a receber R${sal_n:.2f}')