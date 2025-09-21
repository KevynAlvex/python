numIni = int(input('Insira o número inicial: '))
razao = int(input('Insira a razão: '))
print(numIni, end=' >> ')
for i in range(0,9):
    pa = numIni + razao
    print(pa,end=' >> ')
    numIni += razao

print('FIM')