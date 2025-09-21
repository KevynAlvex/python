from datetime import date

maiores = 0
menores = 0
for i in range(1, 8):
    idade = date.today().year - int(input('Ano de nascimento: '))
    if idade >= 18:
        maiores +=1
    else:
        menores +=1

print(f'Menores de idade: {menores}\nMaiores de idade: {maiores}')
