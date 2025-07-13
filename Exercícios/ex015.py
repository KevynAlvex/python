dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
v_pg = (dia * 60) + (km * 0.15)
print(f'O total a pagar é de R${v_pg:.2f}.')