while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    if num < 0:
        break
    print('-'*30)
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
    print('-' * 30)
print('-'*30)
print('Programa encerrado!')