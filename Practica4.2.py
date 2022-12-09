# Practica #2
string_word1 = input('ingresar la oracion:')
counter = 0
string_word = string_word1.split( )

print(string_word)

for word in string_word1:
        counter += 1
        print('la primera palabra es:', word, 'es', word[0].title())

        if counter == 1: 
                first_1_word_1= word[0].title()
                word_1_next_word= word[0].title()
                print('la primera letra de la palabra descrita:', word_1_next_word, ';la primera letra de la segunda palabra descrita:', word_1_next_word )
                print(' ')
        
        else:
                word_1_next_word= word[0].title()
                print('la primera letra de la palabra descrita:', word_1_next_word, ';la primera letra de la segunda palabra descrita:', word_1_next_word )
        
                if word_1_next_word != first_1_word_1:
                        print('True, si es un taerograma')
                        quit()







    