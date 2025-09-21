from statistics import mean

nomes = []
idades = []
sexos = []

for i in range(1,5):
    print(f'PESSOA {i}'.center(25,'-'))
    nome = input('Nome: ').strip().capitalize()
    nomes.append(nome)
    idade = int(input('Idade: '))
    idades.append(idade)
    while True:
        sexo = input('Sexo [F/M]: ').strip().upper()
        if sexo != 'F' and sexo != 'M':
            print('Insira apenas F ou M!')
        else:
            sexos.append(sexo)
            break

media = mean(idades)
WomanLessTwenty = 0
older = 0
older_name = ''
for name, age, gender in zip(nomes, idades, sexos):
    if gender == 'M':
        if age > older:
            older = age
            older_name = name

    if gender == 'F':
        if age < 20:
            WomanLessTwenty +=1

print('-'*25)
print(f'A média de idade desse grupo é de {media} anos!')
print(f'O homem mais velho se chama {older_name} com {older} anos de idade!')
print(f'Existem {WomanLessTwenty} mulheres com menos de 20 anos!')