import base_words
import random

def user_name_builder():

    words_list= base_words.get_medium_words() + base_words.get_large_words()

    names_list = []

    # Filter words by length. Add those to words to empty names list.
    for word in words_list:
        if len(word) <= 8:
            names_list.append(word)
        else:
            pass

    # Define a random int between 1 and large word list length.
    rand_nf = random.randint(1,len(names_list))
    rand_nl = random.randint(1,len(names_list))

    # Pick a random word from the list.
    first_name = names_list[rand_nf]
    last_name = names_list[rand_nl]

    first_name = first_name.title()
    last_name = last_name.title()

    name:dict = {'first_name': first_name , 'last_name': last_name}

    return name

print(user_name_builder())