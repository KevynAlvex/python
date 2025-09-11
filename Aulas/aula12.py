nome = input('Qual é o seu nome? ')
if nome == 'Kevyn':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Nome popular')
elif nome in 'Ana Claudia Mara Maria':
    print("belo nome feminino")

print(f"Tenha um bom dia {nome}!")