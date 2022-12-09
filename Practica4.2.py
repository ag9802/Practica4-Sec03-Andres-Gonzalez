string_word1 = input('ingresar la oracion:')

string_word = string_word1.split( )

print(string_word)

string_word_1 = string_word[0]
string_word_2 = string_word[1]
string_word_3 = string_word[2]
string_word_4 = string_word[3]

if set(string_word_1) == set(string_word_2) == set(string_word_3) == set(string_word_4):
        print('true')
else:
        print('false')



    