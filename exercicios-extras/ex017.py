v = float(input('Qual a velocidade do carro em Km/H? '))
if v > 80:
    multa = (v - 80) * 5
    print(f'Você foi multado\nTerá que pagar uma multa de R${multa:.2f}!')
else:
    print('Velocidade adequada!')