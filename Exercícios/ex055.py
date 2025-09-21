maior = 0
menor = 0
# verificar = []
for i in range(1,6):
    peso = float(input(f'Peso da {i}º pessoa: '))
    # verificar.append(peso)
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print(f'Maior peso: {maior}kg\nMenor peso: {menor}kg')
# print(f'LMAIOR: {max(verificar)} e LMENOR: {min(verificar)}')
