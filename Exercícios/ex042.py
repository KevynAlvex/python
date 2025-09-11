def triangulos(seg1, seg2, seg3):
    if (seg1+seg2) > seg3 and (seg2+seg3) > seg1 and (seg3+seg1) > seg2:
        print('É possível formar um triângulo', end=' ')
        if seg1 == seg2 == seg3:
            print('EQUILATERO')
        elif seg2 == seg1 or seg2 == seg3 or seg3 == seg1 :
            print('ISÓSCELES')
        else:
            print('ESCALENO')
    else:
        print('Não é Possivel formar um triângulo!')


a = float(input('Insira o primeiro segmento: '))
b = float(input('Insira o segundo segmento: '))
c = float(input('Insira o terceiro segmento: '))
triangulos(a,b,c)