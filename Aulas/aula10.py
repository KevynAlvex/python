n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}')
if (m >= 5) and (m <= 7.9):
    print('Você está na média!')
elif m > 8:
    print('A sua média foi boa! Parabéns')
else:
    print('Sua nota está ruim!')