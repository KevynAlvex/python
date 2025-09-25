print('Gerador de PA'.center(25,'='))
cont = 10
num = int(input("Insira o primeiro termo da PA: "))
r = int(input("Insira a razão: "))
vzs = cont
while cont != 0:
    c = 1
    while c <= cont:
        tC = num + (c-1) * r
        print(tC, end=' -> ')
        c+=1
    print('Pausa')
    cont = int(input('Quantos termos quer mostrar a mais? '))
    if cont != 0:
        vzs += cont
        num = tC+r
print(f'\nPA finalizada com {vzs} termos mostrados!')