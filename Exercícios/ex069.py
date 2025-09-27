def cabeca():
    print('=' * 30)
    print('Cadastre uma pessoa'.center(30))
    print('=' * 30)

homem = 0
mulher_l20 = 0
g18 = 0


while True:
    cabeca()

    idade = int(input("Idade: "))
    while True:
        sexo = input("Sexo: [M/F] ").strip().upper()
        if sexo in(['M','F']):
            break
        else:
            print('Apenas F ou M!')

    if idade > 18:
        g18 += 1

    if idade <18 and sexo == 'F':
        mulher_l20 += 1

    if sexo == 'M':
        homem += 1

    print('=' * 30)
    while True:
        cont = input("Quer continuar? [S/N] ").strip().upper()
        if cont not in(['S','N']):
            print('Apenas S ou N!')
        else:
            break

    if cont == "N":
        break

print(f'Total de pessoas maiores que 18 anos: {g18}')
print(f'Total de HOMENS cadastrados: {homem}')
print(f'Total de MULHERES COM MENOS DE 20 ANOS: {mulher_l20}')