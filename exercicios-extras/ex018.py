from datetime import date
idade = int(input('Em qual ano você nasceu? '))
if date.today().year - idade >= 18:
    print('Você tem mais de 18 anos!\nPortanto deve votar!')
else:
    print('Você ainda não pode votar!')