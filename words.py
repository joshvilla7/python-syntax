def print_upper_words(words):
    """ this function takes in a word(s) and uppercases it 
    and prints each word on a separate line """

    for word in words:
        print(word.upper())


def print_lettered_words(words, starts_with):
    """ this function prints a word and uppercases it
    based on the letter it starts with in the argument """

    for word in words:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())

