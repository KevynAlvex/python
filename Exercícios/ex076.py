materiais = (('Tesoura', 5.60),('Lápis', 1.75),('Borracha', 0.75),('Caderno', 50.90),('Estojo', 15.75),
             ('Transferidor', 7.80), ('Mochila', 250.99))

print('-'*45)
print('Lista de materiais'.center(45))
print('-'*45)
for item, preco in materiais:
    print(f' {item:.<35}R${preco:>7.2f}')

print('-'*45)