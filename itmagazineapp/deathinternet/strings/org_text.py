# Lorem Ipsum 1000 words.
from base_text import base_text
import random

def words_from_text(text:str):

    #Use returned string from base_text function.
    sentence = text
    
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

    #print ("*** words: ",words)
    #print ("*** number unique words: ", len(words))

    return words

def get_small_words(words:list):

    base_list_words:list = words

    small_words_list = []

    for word in base_list_words:
        if len(word) <= 3:
            small_words_list.append(word)
        else:
            pass

    #Test
    #print ("get small words " , small_words_list, (len(small_words_list)), "words.")

    return small_words_list

def get_medium_words(words:list):
    base_list_words:list = words

    medium_words_list = []

    for word in base_list_words:
        if 4 <= len(word) <= 8:
            medium_words_list.append(word)
        else:
            pass

    #Test
    #print ("getting medium words " , medium_words_list, (len(medium_words_list)), "words.")

    return medium_words_list

def get_large_words(words:list):

    base_list_words:list = words

    large_words_list = []

    for word in base_list_words:
        if len(word) >= 9:
            large_words_list.append(word)
        else:
            pass

    #Test
    #print ("get large words " , large_words_list, (len(large_words_list)), "words.")

    return large_words_list

def user_name_builder(words:str):

    words_list= get_medium_words(words) + get_large_words(words)

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

    # Test
    print(name)

    return name

def sentence_builder(words:str):

    #Inside function sentence block builder.
    def sentence_block_builder():
    
        small_words_list  = get_small_words(words) 
        medium_words_list = get_medium_words(words) 
        large_words_list  = get_large_words(words) 

        ### Rename Me!!!
        # Define quantity of words for each size (small,medium,large)
        # Zero (0) can create an empty set, prone to errors, so initialization must be required.

        # Define collections (set) of words for each size (small,medium,large)
        # Set because we don't want repeated words.
        words_s = set(' ')
        words_m = set(' ')
        words_l = set(' ')

        ### Rename Me!!!
        # Random number of items to extract from list small words
        rand_as = random.randint(0,2)

        # Random number of items to extract from list medium words
        rand_am = random.randint(1,3)

        # Random number of items to extract from list large words
        rand_al = random.randint(0,1)
    
        ### Rename Me!!!
        # Select just one random word from each size list between 0 and list lengh.
        # add words x random times

        # Small words
        for i in range(rand_as):

            small_word  = small_words_list[random.randint(0,len(small_words_list)-1)]
            words_s.add(small_word)

        # Medium words
        for i in range(rand_am):

            medium_word = medium_words_list[random.randint(0,len(medium_words_list)-1)]
            words_m.add(medium_word)

        # Long words
        for i in range(rand_al):

            large_word = large_words_list[random.randint(0,len(large_words_list)-1)]
            words_l.add(large_word)

        ## Build block
        # Join three set in one list
        sentence_block = list(words_s | words_m | words_l)

        # Remove any ' ' in the list.
        for word in sentence_block:
            if word != ' ':
                pass
            else:
                sentence_block.remove(word)

        return sentence_block
    
    sentence: list = []

    # Create two sentence blocks
    for i in range (2):

        sentence = sentence + sentence_block_builder()

    # Add a period to the last two block sentences.
    sentence = sentence + ['.']

    # Create one sentence block.
    sentence = sentence + sentence_block_builder()

    # Add a comma to the last block sentence.
    sentence = sentence + [',']

    # Add two more sentence blocks.
    for i in range (2):

        sentence = sentence + sentence_block_builder()

    # Add period in the first sentence block.
    #sentence = sentence + ['.']

    # Convert a list into one string.
    sentence = ' '.join(sentence)

    # Capitalize sentnce.
    sentence = str.capitalize(sentence)

    return sentence

def paragraph_builder(words:str):
    
    paragraph = ''

    # Create two sentence blocks
    for i in range (10):

        paragraph = paragraph + sentence_builder(words)
    
    return paragraph

def article_builder(words:str):

    article = ''

    # Create two sentence blocks
    for i in range (10):

        article = article + paragraph_builder(words)+ '\n' + '\n'
    
    return article


# Python script
my_words=words_from_text(base_text())

#get_short_words(my_words)
    
print(article_builder(my_words))