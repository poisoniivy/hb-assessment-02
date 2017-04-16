"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    # Creating a list of all the words from the phrase
    phrase_list = phrase.split()
    # Creating an empty dictionary to store words and their counts
    phrase_dict = {}

    # Iterating through the list of words and looking at each word
    for word in phrase_list:
        # Adding the word in the dictionary and incrementing the value by 1
        phrase_dict[word] = phrase_dict.get(word, 0) + 1

    return phrase_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    # Creating the melon dictionary from the info above
    melon_dict = {
        "Watermelon": 2.95,
        "Cantaloupe": 2.50,
        "Musk": 3.25,
        "Christmas": 14.25,
    }

    # Returning the price, or else the phrase "No price found"
    return melon_dict.get(melon_name, "No price found")


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """
    # Dictionary that has word length as key and list of words as values
    length_dict = {}

    # Iterating through each word in the words argument
    for word in words:
        # Assigning the key as the length of each word
        length_key = len(word)
        # Dictionary valie is sorted list of the words based on key
        # Adding a new word to the end of the list of values
        length_dict[length_key] = (
            sorted(length_dict.setdefault(length_key, []) + [word]))

    # Returning sorted tuples of all the items
    return sorted(length_dict.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    eng_to_pirate = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
    }
    # The string that we are returning translated to pirate speak
    pirate_talk = ""
    # Creating a list of the original English words from phrase
    phrase_list = phrase.split()

    # Iterating through the list of English words from phrase
    i = 0
    while i < len(phrase_list):
        # Using variable word for the current word we are translating
        word = phrase_list[i]

        # If the word is in our translation dictionary, add to phrase
        if word in eng_to_pirate:
            pirate_talk += eng_to_pirate[word]
        # If not, add original english word
        else:
            pirate_talk += word
        # Add spaces between words if it's not at end of the list
        if i != len(phrase_list) - 1:
                pirate_talk += " "
        i += 1

    return pirate_talk


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # Creating dictionary of words with starting letter as key
    # Words in values list appear in order of names
    word_lookup = {}

    # The results word list from the game
    results = []

    # Creating a dictionary of words before playing game
    for word in names:
        first_letter = word[0]
        word_lookup.setdefault(first_letter, []).append(word)

    # Setting up game. The first word to look up is the first word in names
    last_letter = names[0][0]

    # Playing until there are no more words in a list to lookup
    # or there are no words to look up from the last letter
    while(last_letter in word_lookup and word_lookup[last_letter] != []):
        # This is the next word to add to the results
        next_word = word_lookup[last_letter][0]
        results.append(next_word)
        # Removing the word from the lookup dictionary
        word_lookup[last_letter] = word_lookup[last_letter][1:]
        # Setting up the next word to look up based on the last letter
        last_letter = next_word[-1]

    return results

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
