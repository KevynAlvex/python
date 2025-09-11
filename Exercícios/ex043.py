def IMC(imc):
    if 18.5 <= imc < 25:
        return 'PESO IDEAL!'
    elif 25 <= imc < 30:
        return 'SOBREPESO!'
    elif 30 <= imc < 40:
        return 'OBESIDADE!'
    elif imc >= 40:
        return 'OBESIDADE MÓRBIDA!'
    else:
        return 'ABAIXO DO PESO'

def cabeca():
    print('='*40)
    print('CLASSIFICAÇÃO IMC'.center(40))
    print('=' * 40)

cabeca()
peso = float(input('Insira seu peso (kg): '))
altura = float(input('Insira sua altura (cm): '))/100
imc = peso / pow(altura,2)
print('='*40)
print(f'Altura: {altura}m\nPeso: {peso}kg')
print(f'IMC: {imc:.1f}\nClassificação: {IMC(imc)}')