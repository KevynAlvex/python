a = float(input('Segmento 1: '))
b = float(input('Segmento 2: '))
c = float(input('Segmento 3: '))

if (a + b > c) and (a + c > b) and (c + b > a):
    print('É POSSIVEL formar um triângulo!')
else:
    print('NÃO É possível formar um triângulo!')
