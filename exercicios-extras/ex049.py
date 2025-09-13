print("="*30)
c = 1
pares = 0
impares = 0
n_p = []
n_i = []
while c <= 6:
    numero = int(input(f'Digite o {c}º número: '))
    if numero %2 == 0:
        pares += 1
        n_p.append(numero)
    if numero %2 == 1:
        impares += 1
        n_i.append(numero)
    c+=1
print('='*30)
print(f"Dos números digitados:\n"
      f"{pares} foram pares {n_p}\n"
      f"{impares} foram ímpares {n_i}")