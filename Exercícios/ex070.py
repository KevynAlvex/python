def cabeca():
    print('='*30)
    print('LOJA BARATISSOMO'.center(30))
    print('=' * 30)

tot_compra = gt_mil  = 0
m_barato = ['', 0]

cabeca()

while True:
    produto = input('Nome do produto: ').strip().capitalize()
    preco = float(input('Preço: R$'))
    tot_compra += preco

    if m_barato[1] == 0:
        m_barato[1] = preco

    if preco < m_barato[1]:
        m_barato[1] = preco
        m_barato[0] = produto

    if preco > 1000:
        gt_mil += 1

    while True:
        cont = input('Quer continuar? [S/N] : ').strip().upper()
        if cont in (['S', 'N']):
            break
        else:
            print('Apenas S ou N!')

    if cont == 'N':
        break
    else:
        continue

print('FIM DO PROGRAMA'.center(30,'='))

print(f'O total da sua compra foi de R${tot_compra:.2f}')
print(f'Temos {gt_mil} produtos custando mais que R$1000.00')
print(f'O produto mais barato foi "{m_barato[0]}" custando R${m_barato[1]}')