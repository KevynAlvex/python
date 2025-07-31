def tinta(a, b):
    tinta = a*b/2
    return f'Serão necessários {tinta:.2f} litros de tinta para pintar!'

l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))

print(f'Sua parede tem as dimensões de {l}x{h} com uma área de {l*h:.2f}m²')
print(tinta(l, h))
