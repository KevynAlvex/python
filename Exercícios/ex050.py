s_p = 0
for i in range(1,7):
    num = int(input(f'Insira o {i}º número: '))
    if num % 2 == 0 :
        s_p+=num
    else:
        continue

print(f'A soma dos números pares é {s_p}')