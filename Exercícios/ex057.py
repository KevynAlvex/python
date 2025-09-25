while True:
    sexo = input("Informe seu sexo [F/M]: ").strip().upper()
    if sexo in ('MF'):
        print(f'Sexo {sexo} registrado com sucesso!')
        break
    else:
        print('Dados inválidos, informe apenas F ou M !')