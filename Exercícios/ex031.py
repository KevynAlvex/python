#Perguntando a distância
dist = float(input('Qual a distância de sua viagem? '))
print(f'Você está prestes a começar sua viagem de {dist} KM!')
print('E o preço da sua passagem será de R$', f'{dist*0.5:.2f}'if dist < 200 else f'{dist*0.45:.2f}' )