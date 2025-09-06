num_ini = int(input('Digite o número inicial: '))
num_fin = int(input("Digite o número final: "))
incremento = int(input("Digite o incremento: "))

if num_ini > num_fin:
    while num_ini >= num_fin:
        print(num_ini, end=' ')
        num_ini -= incremento
    print('ACABOU!')
else:
    while num_ini <= num_fin:
        print(num_ini, end= ' ')
        num_ini += incremento
    print('ACABOU!')