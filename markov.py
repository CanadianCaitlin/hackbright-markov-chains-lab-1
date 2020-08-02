"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
 
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    # purpose of function: split the string into tuples
    # chains.get(string_tups,[])
    # chains[string_tups].append(text_string[i+2])

    #if string_tups is not in the dictionary:
        #set dictionary[string_tups] = []
    #else if string_tup is in the dict:
        #append the value to dictionary[string_tups] (list)
    
    # for i in chains.items():
    #     print(i)
    # print(chains)

    chains = {}

    text_string = text_string.split()

    for i in range(len(text_string)-2):
        string_tup = (text_string[i], text_string[i+1])

        chains[string_tup] = chains.get(string_tup, [])
        chains[string_tup].append(text_string[i+2])

    return chains


def make_text(chains):
    """Return text from chains."""

    # words is our empty list which will be printed as a string

    #first creating a word link(list)
        #if words is emtpy:
            #loop thru chains to get a key
            #words append key and also a random value from chains[key]
                #now the words is not empty
        #elif words is not empty:
            #identify last 2 strings; see if they match a key in the dictionary
            #choose random value from list of key values 
            #append random value to words list
    # keep looping until "KeyError"

    # random.choice(<dictionary>.keys())
    # list(dictionary.keys())

    words = []
    dict_keys = list(chains.keys()) #a list of all the dictionary keys
    while True:
    
        first_key = choice(dict_keys) #first key == a random key from the above list
        word1, word2 = first_key #unpack
        if word1[0].isupper() == True:
            words.append(word1)
            words.append(word2)
            words.append(choice(chains[first_key])) #append random value from that random key 
            break
        else:
            pass
    #have a word list that 3 words. 1st word would be a capitalized word

    while True:
        last_two_words = tuple(words[-2:])  #turn last 2 strings into a tuple
        w1, w2 = last_two_words
        if w2[-1].isalpha() == False:
                # if w2[-1] == "?" or w2[-1] == "!" or w2[-1] == ".":
            break
            #if last letter of second word is not a letter, break the loop
        elif last_two_words in chains:
            # w1, w2 = last_two_words
            words.append(choice(chains[last_two_words]))
            # if w2[-1].isalpha() is False:
            #     # if w2[-1] == "?" or w2[-1] == "!" or w2[-1] == ".":
            #     break
            # else: 
            #     pass
                
                #adding an elif statement looking for the last letter of the 2nd word of the key
                     #break
        else:
            break
            #identify last 2 strings; see if they match a key in the dictionary
            #choose random value from list of key values 
            #append random value to words list
            #else: break


    # if words == []:
    #     for key in chains:
    #         word_one, word_2 = key
    #         # words.append(word_one)
    #         words.append(word_2)
    #         random_value = chains[key]
    #         words.append(choice(random_value))

    # return words
    return " ".join(words)


input_path = "green-eggs.txt"
# input_path = sys.argv[1]


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
