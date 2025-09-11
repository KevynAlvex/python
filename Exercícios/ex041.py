from datetime import date

def categorias(idade):
    if 20 <= idade <= 25:
        return 'Sênior'
    elif 15 <= idade <= 19:
        return 'Júnior'
    elif 10 <= idade <= 14:
        return 'Infantil'
    elif idade <= 9:
        return 'Mirim'
    elif idade > 25:
        return 'Master'
    else:
        print('Houve algum erro!')

def cabeca():
    print('='*35)
    print('CLASSIFICAÇÕES'.center(35))
    print('='*35)

cabeca()
idade = date.today().year - int(input('Digite o ano de nascimento: '))
print(f'O atleta tem {idade} anos.')
classe = categorias(idade)
print(f'CLASSIFICAÇÃO: {classe}')