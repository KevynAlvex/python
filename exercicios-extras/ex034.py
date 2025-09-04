from unicodedata import category

h = int(input('Insira a sua altura em centimetros: '))/100
kg = float(input('Insira seu peso em kilos: '))
imc = kg/(pow(h,2))
print(f'Seu IMC é: {imc:.2f}')
if imc > 40:
    categoria = 'Obesidade mórbida'
if 30 < imc <= 40:
    categoria = 'Obesidade'
if 25 < imc <= 30:
    categoria = 'Sobrepeso'
if 18.5 <= imc < 25:
    categoria = 'Peso Ideal'
if imc < 18.5:
    categoria = 'Abaixo do peso'
print(f'Isso diz que você está '+ f'{categoria}')

