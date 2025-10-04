# () <-- Tuplas
# [] <-- Listas
# {} <-- Dictionarios

'''

lanche = ('Hambúrguer', 'Suco','Pizza', 'Pudim', 'Batata Frita')

# Errado: lanche[1] = "Guaraná"

print(lanche)
print(lanche[1:])
print(lanche[:2])
print(lanche[1])
print(lanche[-1])

print()

for i in lanche:
    print(f'Eu vou comer {i}')

print()

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}')

print()

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print()

print(sorted(lanche))

'''
'''
a = (1,2,3)
b = (1,3,5,7)
c = a + b
d = b + a
print(c, '\n', d)
print(len(c))
print(c.count(9))
print(c.index(5))
'''
pessoa = ('Kevyn', 18, 'M', 69.69)
print(pessoa)
del(pessoa)
