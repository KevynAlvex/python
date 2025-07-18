sentence = input('Write a sentence: ').strip().upper()
sA = sentence.count('A') + sentence.count('Á') + sentence.count('À')
print(f'''A letra A aparece {sA} vezes na frase.
A primeira letra a aparece na posição {sentence.find('A') + 1}
A ultima letra a aparece na posição {sentence.rfind('A') + 1}''')

#só precisei de ajuda no .rfind(), não lembrava dele