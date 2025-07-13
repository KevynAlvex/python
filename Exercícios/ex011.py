def area(l, h):
    return l*h

def qnt(a):
    return a/2

l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = area(l, h)
t = qnt(a)
print(f'Sua parede tem a dimensão de {l} x {h} e sua área é de {a:.2f}m².\nPara pintar essa parede, você precisará de {t:.2f}l de tinta.')