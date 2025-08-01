from time import sleep
print('-'*40)
cigar = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('A quantos anos você fuma? '))
print('-'*40)
print('\nCalculando\n')
dias_p = (cigar * (anos*365) * 10) / 1440
sleep(3)
print('-'*40)
print(f'Ao total, você já perdeu {dias_p:.2f} dias de vida')
