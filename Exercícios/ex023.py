num = int(input('Infome um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'''Dissecando o número...
Unidade: {u}  
Dezena: {d}
Centena: {c}
Milhar: {m}''')