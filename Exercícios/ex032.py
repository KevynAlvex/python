from datetime import date #importando datetime p pegar ano atual
#pedindo ano
ano = int(input('Digite um ano qualquer. Ou digite 0 para analizar o ano atual!: '))

#pegando ano atual
if ano == 0:
    ano = date.today().year

#Verificando se o ano é bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
