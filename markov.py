"""Generate markov text from text files."""


from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    opened_file = open(file_path)
    # file_path.close()
    return opened_file.read()

def make_chains(text_string):
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

    for i in range(len(word_list) - 2):
        key_tuple = (word_list[i], word_list[i + 1])
        # if i == len(word_list) - 2:
        #     break
            #chains[key_tuple] = chains.get(key_tuple, []) 
        if key_tuple not in chains:
            chains[key_tuple] = [word_list[i + 2]]
        else:
            chains[key_tuple].append(word_list[i + 2])

    # for item, value in chains.items():
    #     print item, value

    return chains


def make_text(chains):
    """Returns text from chains."""

    key_tuple = choice(chains.keys())
    words = list(key_tuple)

    while True:
        if key_tuple in chains:
            first_item = key_tuple[1]
            value = choice(chains[key_tuple])
            words.append(value)
            key_tuple = (first_item, value)
            # key_tuple = (words[-2], words[-1])
        else:
            break

    return " ".join(words)

    # your code goes here

    #return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

print chains
print
# Produce random text
random_text = make_text(chains)

print random_text
