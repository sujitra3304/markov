"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    opened_file = open(file_path).read()

    return opened_file
# print (open_and_read_file('green-eggs.txt'))

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 2):
        # print (words[2:3])
        chains[(words[i], words[i+1])] = chains.get((words[i], words[i+1]), [])
        
        # chains[(words[i], words[i+1])] += (words[i+2:i+3])
        chains[(words[i], words[i+1])].append(words[i+2])
    # print('CHAINS', chains)
    return chains

# print(make_chains(open_and_read_file('green-eggs.txt')))

def make_text(chains):
    """Return text from chains."""
    # chain_keys = sorted(chains)
    words = []
    # word_link = choice(chain_keys)
    # words = words + list(word_link)
    word_link = choice(list(chains.keys()))
    
    # while True:
    #     if word_link not in chain_keys:
    #         break
    while word_link in chains:

        # create variable that equals random value of key(word_link)
        # append variable of key(word_link) from chains to words(list)
        # redefine word_link variable to equal second index of word_link & the random variable

        random_key_value = choice(chains[word_link])
        words.append(random_key_value)
        word_link = (word_link[1], random_key_value)
    

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
