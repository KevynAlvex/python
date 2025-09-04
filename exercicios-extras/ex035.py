def cabeca():
    print('='*25)
    print('ALUGUEL DE CARRO'.center(20))
    print('='*25)
    print('[1] - Carro Popular')
    print('[2] - Carro de Luxo')
    print('='*25)

cabeca()

#Escolha do carro para que possa ser possível determinar o valor
valor_carro = 0
verificador = True
while verificador:
    t_car = int(input('R: '))
    if t_car == 1 or t_car == 2:
        if t_car == 1:
            valor_carro += 90
        if t_car == 2:
            valor_carro += 150
        verificador = False
    else:
        print('Escolha apenas as opções acima!')
        continue

#Pegando dias
dias = int(input('Por quantos dias o carro foi usado? '))*valor_carro #<- Multiplica automaticamente o valor do aluguel

#Pegando e calculando os kM's
km = float(input('Quantos quilometros foram percorridos? '))
kmt = km
if valor_carro == 90: #Para carros populares
    if km > 100:
        km*=0.1
    else:
        km*=0.2

if valor_carro == 150: #Para carros de luxo
    if km > 200:
        km*=0.25
    else:
        km*=0.3

#SOMATÓRIA FINAL/TOTAL
valor_total = dias + km

#output
print('='*20)
print(f'''Você alugou o carro por {dias/valor_carro:.0f} dias e
Rodou {kmt} KM
Então o total que tem que pagar é R${valor_total:.2f}''')

