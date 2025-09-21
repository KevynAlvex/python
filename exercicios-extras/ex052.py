print("Idades".center(30,'='))
c = 1
soma = 0
maior_18 = 0
menos_5 = 0
maior = 0
while c <= 10:
    idade = int(input(f"Insira a {c}º idade: "))
    soma += idade
    if idade > 18:
        maior_18 +=1
    if idade < 5:
        menos_5 += 1

    if c == 1:
        maior = idade
    else:
        if idade > maior:
            maior = idade

    c +=1


media = soma/10

print(f"Média entre as idades: {media:.1f}\n"
      f"Mais de 18 anos: {maior_18}\n"
      f"Menor que 5 anos: {menos_5}\n"
      f"Maior idade: {maior} anos!")