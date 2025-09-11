from datetime import date
ano_atual = date.today().year
idade = ano_atual - int(input('Ano de nascimento: '))

print(f'Quem nasceu em {ano_atual - idade} faz {idade} anos em {ano_atual}')

if idade == 18:
    print('Portanto, deverá alistar-se já!')
elif idade < 18:
    print(f'Ainda faltam {18-idade} anos para você se alistar!')
else:
    print(f'Caso não tenha se alistado com essa idade, deverá ir o mais rápido possivel!')
    print(f'Está atrasado faz {idade-18} anos!')
