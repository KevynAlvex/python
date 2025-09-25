num = int(input('Digite um número [999 para parar] : '))
soma = num
cont = 1
while num != 999:
    num = int(input('Digite um número [999 para parar] : '))
    if num != 999:
        soma += num
        cont +=1

if cont == 1:
    print(f'Você digitou somente um número! Que é {num}!')
else:
    print(f'Você digitou {cont} números!\nA soma entre eles é {soma}')
