word_1 = input('ingresar la primera palabra:')
word_2 = input('ingresar la segunda palabra:')

print('¿los pares de palabras son anagramas?')

if set(word_1) == set(word_2) :
    print('Efectivamente las palabras suministradas forman anagramas')
else:
    print('Error, las palabras no forman anagramas')