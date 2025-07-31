def media(a, b):
    media = (a+b)/2
    return media

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print(f'A média entre as notas {nota1} e {nota2} é {media(nota1, nota2):.1f}')