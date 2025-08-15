l = float(input('Insira a largura do terreno em metros: '))
c = float(input('Insira o comprimento do terreno em metros: '))
area = l*c

if area >= 100 and area <=500:
    print('Terreno Master')
elif area < 100:
    print('Terreno Popular')
else:
    print('Terreno VIP')
