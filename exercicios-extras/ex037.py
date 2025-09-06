def get_dados():
    nome = input('Nome do funcionário(a): ').strip()
    c = True
    while c:
        genero = input('Gênero do funcionário(a) [F/M]: ').strip().upper()
        if genero != 'F' and genero != 'M':
            print('Apenas F ou M!')
            continue
        else:
            c = False
    anos_casa = int(input('Anos de empresa do funcionário(a): '))
    sal_atual = float(input('Salário atual do funcionário(a): R$'))

    dados = (nome, genero, anos_casa, sal_atual)

    return dados

def print_dados(nome, sal_novo, genero, anos,):
    print('='*35)
    print('Dados do Funcionário com salário atualizado:')
    print(f"Nome: {nome}\nGênero: {'Feminino' if genero == 'F' else 'Masculino'}")
    print(f"Anos de empresa: {anos} anos\nSalário: R${sal_novo}")
    print('=' * 35)

def aumento(genero, anos, sal_atual):
    sal_aumento = sal_atual
    if genero == 'M': #For Man
        if anos < 20:
            sal_aumento *= 1.03
        if anos > 30:
            sal_aumento *= 1.25
        if 20 <= anos <= 30:
            sal_aumento *= 1.12

    if genero == 'F': #For Woman
        if anos < 15:
            sal_aumento *= 1.05
        if anos > 20:
            sal_aumento *= 1.23
        if 15 <= anos <= 20:
            sal_aumento *= 1.12

    return sal_aumento

dados = get_dados()
aumento = aumento(dados[1], dados[2], dados[3])
print_dados(dados[0],aumento,dados[1],dados[2])