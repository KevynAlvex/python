print('+---'*10)
print('              AutoLocadora')
print('+---'*10)
kms = float(input('Quantos KM foram rodados com o carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
tot_pag = (dias * 90) + (kms*0.2)
print('+---+'*20)
print(f'''Dias Alugados: {dias} - R${dias*90:.2f}
Km rodados: {kms} - R${kms*0.2:.2f}
Total a pagar: R${tot_pag:.2f}''')