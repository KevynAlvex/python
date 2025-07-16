cidade = str(input('Escreva o nome de uma cidade: ')).strip().lower()
verif = 'santo' in cidade[:5]
print(f'O nome da cidade começa com "Santo?": \n{verif}')
