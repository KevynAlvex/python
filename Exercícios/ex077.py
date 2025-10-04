palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')

vogais = ('a',
          'e',
          'i',
          'o',
          'u')

for i in palavras:
    print(f'Na palavra {i} temos',end=' ')
    for j in i.lower():
        if j in vogais:
            print(f'{j}', end='')
    print( )