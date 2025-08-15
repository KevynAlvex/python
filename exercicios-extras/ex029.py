nome = input('Digite o nome do funcionário: ').strip()
sal = float(input('Informe o salário do funcionário: R$'))
anos = int(input('A quantos anos o(a) sr.(a) {} trabalha na empresa? '.format(nome)))

if anos >= 3 and anos <= 10:
    print('O funcionário(a) {} que trabalha a {} anos'.format(nome, anos))
    print('Receberá 12.5% de aumento, passando a ganhar R${:.2f}'.format(sal*1.125))
elif anos < 3:
    print('O funcionário(a) {} que trabalha a {} anos'.format(nome, anos))
    print('Receberá 3% de aumento, passando a ganhar R${:.2f}'.format(sal*1.03))
else:
    print('O funcionário(a) {} que trabalha a {} anos'.format(nome, anos))
    print('Receberá 20% de aumento, passando a ganhar R${:.2f}'.format(sal*1.2))  