soma = 0
num_d = 0
while True:
    numero = int(input("Digite um número (999 para parar) : "))
    if numero == 999:
        break
    soma += numero
    num_d += 1
print(f"Foram digitados {num_d} números e a soma deles é {soma}")
