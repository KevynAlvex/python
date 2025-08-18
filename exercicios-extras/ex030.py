AB = float(input('Insira o tamanho do primeiro segmento: '))
BC = float(input('Insira o tamanho do segundo segmento: '))
CA = float(input('Insira o tamanho do terceiro segmento: '))

if (AB + BC > CA) and (BC + CA > AB) and (AB + CA > BC):
    form = ''
    if AB == BC == CA:
        form = 'Equilátero'
    elif (AB == BC) or (BC == CA) or (AB == CA):
        form = 'Isóceles'
    if AB != BC != CA:
        form = 'Escaleno'

    print(f'É possível formar um triângulo {form}!')

else:
    print('Não é possivel formar um triângulo!')