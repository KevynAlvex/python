from math import sin, cos, radians, tan
a = float(input('Digite um ângulo: '))
sens = sin(radians(a))
coss = cos(radians(a))
tans = tan(radians(a))
print(f'Para o Ângulo de {a}º temos:')
print(f'Seno: {sens:.2f}\nCosseno: {coss:.2f}\nTangente: {tans:.2f}')

