from random import randint
def sortear():
    numeros = []
    c = 1
    while c <= 20:
        numeros.append(randint(0,10))
        c+=1
    return numeros

def printar(numeros):
    print("Números sorteados: ", end='')
    gtf = 0
    gtfl = []
    qnt3 = 0
    np3 = []
    for i in numeros:
        print(i, end = ' ')
        if i > 5:
            gtfl.append(i)
            gtf += 1
        if i %3 == 0:
            np3.append(i)
            qnt3 +=1

    print(f"\nForam {gtf} números acima de 5 {gtfl}")
    print(f"Ao total foram {qnt3} números divisíveis por 3 {np3}")


numeros = sortear()
printar(numeros)