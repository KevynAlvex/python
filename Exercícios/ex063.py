def cabeca():
    print('-'*30)
    print('SEQUÊNCIA DE FIBONACCI'.center(30))
    print('-' * 30)

def fibonacci():
    termos = int(input('Quantos termos quer mostrar? '))
    c = 1
    termo1 = 0
    termo2 = 1
    print('~'*30)
    print(f'{termo1} -> {termo2}',end=' -> ')
    while c <= (termos-2):
        termo3 = termo1 + termo2
        termo1 = termo2
        termo2 = termo3
        print(termo3, end=' -> ')
        c+=1
    print('FIM')
    print('~' * 30)
cabeca()
fibonacci()