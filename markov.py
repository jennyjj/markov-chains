"""Generate markov text from text files."""


from random import choice
import sys 


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    opened_file = open(file_path)
    # file_path.close()
    return opened_file.read()

def make_chains(text_string, n_grams):
    """Takes input text as string; returns dictionary of markov chains.

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
    """

    chains = {}

    word_list = text_string.split()

    for i in range(len(word_list) - n_grams):
        key_tuple = tuple(word_list[i: i + n_grams])

        if key_tuple not in chains:
            chains[key_tuple] = [word_list[i + n_grams]]
        else:
            chains[key_tuple].append(word_list[i + n_grams])

    for item, value in chains.items():
        print item, value

    return chains


def make_text(chains, n_grams):
    """Returns text from chains."""

    key_tuple = choice(chains.keys())
    words = list(key_tuple)

    while True:
        if key_tuple in chains:
            words.append(choice(chains[key_tuple]))
            key_tuple = tuple(words[-n_grams:])
        else:
            break

    return " ".join(words)

    # your code goes here

    #return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 2)

# print chains
print
# Produce random text
random_text = make_text(chains, 2)

print random_text
