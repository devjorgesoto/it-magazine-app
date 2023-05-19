import base_words

import random

def sentence_builder():

    #Inside function sentence block builder.
    def sentence_block_builder():
    
        small_words_list  = base_words.get_small_words() 
        medium_words_list = base_words.get_medium_words() 
        large_words_list  = base_words.get_large_words() 

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
    
    # final sentence, returned at the function end.
    sentence: list = []

    # create sentence blocks 
    # a full sentence is created with 5 sentence blocks

    block_b1 = sentence_block_builder()
    block_b2 = sentence_block_builder()
    block_b3 = sentence_block_builder()
    block_b4 = sentence_block_builder()
    block_b5 = sentence_block_builder()

    # capitalize
    # capitalize sentence blocks (b1 and b3)

    # b1
    # b1 find the first item in the list (sentence:list)
    b1_first_item:str = block_b1[0] 

    # b1 update last item with a period at the end.
    b1_first_item = str.capitalize(b1_first_item)

    # b1 Add and replace first item in the list with new item updated.
    block_b1[0] = b1_first_item

    # period
    # period at the end in sentence block (b5)

    # b5 find the last item in the list 
    # b5_index means: index of the last item in block b5
    b5_index:int = len(block_b5)-1 
    b5_last_item:str = block_b5[b5_index] 

    # b5 update last item with a period and space at the end.
    b5_last_item = b5_last_item +'. '

    # b5 add and replace last item in the list with new item updated.
    block_b5 [b5_index] = b5_last_item

    # comma
    # comma at the end in sentence block (b3)

    # b3 find the last item in the list
    # b3_index means: index of the last item in block b3
    b3_index:int = len(block_b3)-1 
    b3_last_item:str = block_b3[b3_index] 

    # b2 update last item with a comma at the end.
    b3_last_item = b3_last_item +','

    # b2 add and replace last item in the list with new item updated.
    block_b3 [b3_index] = b3_last_item

    # sentence
    # sentence with every block joined (in order by number)

    sentence = block_b1 + block_b2 + block_b3 + block_b4 + block_b5

    # Convert list into a string.
    sentence = ' '.join(sentence)

    return sentence

def paragraph_builder():
    
    paragraph = ''

    # create a paragraph with 10 sentences.
    for i in range (10):

        paragraph = paragraph + sentence_builder()
    
    return paragraph

def article_builder():

    article = ''

    # Create a article with 10 paragraphs
    for i in range (10):

        article = article + paragraph_builder()+ '\n' + '\n'
    
    return article

# Python script

print(article_builder())