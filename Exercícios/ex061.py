print('Gerador de PA'.center(25,'='))
num = int(input("Insira o primeiro termo da PA: "))
r = int(input("Insira a razão: "))
c = 1
while c <= 10:
    tC = num + (c-1) * r
    print(tC, end=' -> ')
    c+=1
print('Fim')