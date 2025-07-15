nome = str(input('Digite seu nome completo: ')).strip()
nome_div = nome.split()
print(f'''Maiúsculo: {nome.upper()}
Minúsculo: {nome.lower()}
O seu nome tem {len(nome) - nome.count(' ')} letras
Seu primeiro nome é {nome_div[0]} e ele tem {len(nome_div[0])} letras''')
