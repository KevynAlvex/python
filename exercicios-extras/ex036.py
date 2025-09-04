def cabeca():
    print('='*30)
    print('DINHEIRO SAUDÁVEL'.center(30))
    print('=' * 30)

cabeca()
horas = int(input('Qual o total de horas que você se exercitou esse mês? '))
#CALCULANDO OS PONTOS
pontos = 0
if horas <= 10:
    pontos = 2*horas
elif horas > 20:
    pontos = 10*horas
else:
    pontos = 5*horas

#CONTANDO O CASH
ganhos = pontos * 0.05

print('='*30)
print(f'''você se exercitou por {horas} horas esse mês!
Reuniu um total de {pontos} pontos!
Com isso, seus ganhos foram de R${ganhos:.2f}''')