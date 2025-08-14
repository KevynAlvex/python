print('-='*25 + '-')
print('CALCULANDO PASSAGEM'.center(30))
print('-='*25 + '-')

#Coletando Dados
dis = float(input('Qual a distância que você quer percorrer (KM)? '))

#Calculando
if dis <= 200:
    pas = 0.5
    print(f'Como sua viagem é de menor ou igual a 200KM, cobraremos R$0,50 por KMs\nKM: {dis} x R$0,50\nTotal: R${dis*0.5}')
else:
    pas = 0.45
    print(f'Como sua viagem é de maior que 200KM, cobraremos R$0,45 por KMs\nKM: {dis} x R$0,45\nTotal: R${dis*0.45}')
