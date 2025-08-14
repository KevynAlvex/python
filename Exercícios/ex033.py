num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
num3 = int(input('Insita o terceiro número: '))
maior = num1
if num2 > num1 and num2>num3:
    maior = num2
if num3 > num1 and num3>num2:
    maior = num3
menor = num2
if num1 < num2 and num1 < num3:
    menor = num1
if num3 < num2 and num3 < num1:
    menor = num3
print(f'Maior {maior}\nMenor {menor}')