import base_text

def words_from_text():

    #Use returned string from base_text function.
    sentence = base_text.base_text()
    
    #Remove any comma in the string.
    sentence = sentence.replace(',', '')

    #Remove any period in the string.
    sentence = sentence.replace('.', '')

    #Remove any \n in the string.
    sentence = sentence.replace('\n', '')
   
    #Convert any cased characters to lowercase.
    sentence = sentence.lower()
    
    #Create a new list with any characters separated by a space (' '). 
    #So, it's a new list of words is created from a given string.
    words:list = sentence.split(' ')

    # Remove any empty string ('') from the list
    empty_string = ''
    if empty_string in words: words.remove(empty_string)

    #Remove duplicated words in the list with a set collection.
    #Cast set into a list again.
    words =  list(set(words))

    return words

def get_small_words():

    base_list_words:list = words_from_text()

    small_words_list = []

    for word in base_list_words:
        if len(word) <= 3:
            small_words_list.append(word)
        else:
            pass

    return small_words_list

def get_medium_words():
    base_list_words:list = words_from_text()


    medium_words_list = []

    for word in base_list_words:
        if 4 <= len(word) <= 8:
            medium_words_list.append(word)
        else:
            pass

    return medium_words_list

def get_large_words():

    base_list_words:list = words_from_text()

    large_words_list = []

    for word in base_list_words:
        if len(word) >= 9:
            large_words_list.append(word)
        else:
            pass

    return large_words_list
