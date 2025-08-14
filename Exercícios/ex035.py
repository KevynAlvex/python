print('-='*30 + '-')
print('ANALISE DE TRIÂNGULOS'.center)
print('-='*30 + '-')

AB = float(input('Seguimento AB: '))
CD = float(input('Seguimento CD: '))
EF = float(input('Seguimento EF: '))

if (AB + CD > EF) and (CD + EF > AB) and (AB + EF > CD):
    print('Os seguimentos PODEM formar um triangulo!')
else:
    print('Os segumentos NÃO PODEM formar um triângulo!')