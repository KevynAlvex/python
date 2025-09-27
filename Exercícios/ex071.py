# REFAZER DEPOIS

print('-'*30)
print('BANCO B'.center(30))
print('-'*30)

v_total = int(input("Quantos vai sacar? R$"))
tot = v_total
nota = 50
tot_notas = 0
while True:
    if nota <= tot:
        tot -= nota
        tot_notas+=1
    else:
        if tot_notas > 0:
            print(f'Total de {tot_notas} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1

        tot_notas = 0
        if tot == 0:
            break