"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    # Solution using 'set' and 'list' constructor functions
    return list(set(words))

    # Solution using dictionaries
    # no_duplicates = {}

    # i = 0
    # while i < len(words):
    #     if words[i] not in no_duplicates:
    #         no_duplicates[words[i]] = 1
    #     i += 1

    # return no_duplicates.keys()


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    # Set math
    return list(set(items1) & set(items2))

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    # Using sets, lists, tuples to solve
    # pairs = set()
    # i = 0
    # while i < len(numbers):
    #     j = i
    #     while j < len(numbers):
    #         if numbers[i] + numbers[j] == 0:
    #             pair = tuple(sorted([numbers[i], numbers[j]]))
    #             pairs.add(pair)
    #         j += 1
    #     i += 1

    # return list(pairs)

    pairs = {}
    i = 0
    j = 0
    while i < len(numbers):
        # print i
        while j < len(numbers):
            # print "i and j:", numbers[i], numbers[j]
            if (numbers[i] + numbers[j] == 0
                    and numbers[j] not in pairs):
                pairs[numbers[i]] = [numbers[i], numbers[j]]
            j += 1
        j = 0
        i += 1

    return pairs.values()


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    # dictionary of letter as key and number or occurences as value
    char_count = {}
    # dict where number of occurences is key and letter list as values
    num_count = {}
    # NOTE: Used two dictionaries. Could think about a simpler solution

    i = 0

    while i < len(phrase):

        letter = phrase[i]
        # Adding the first letter in the char_count dictionary and
        # appending that letter to the "1" value of num_count dictionary
        if letter not in char_count and letter != " ":
            char_count[letter] = 1
            num_count.setdefault(1, []).append(letter)
        # Increasing number of that letter in char count
        # Removing that letter from previous list in num count to new list
        # need to two dictionaries to look up the number of occurences
        elif letter != " ":
            num_count_key = char_count[letter]
            num_count[num_count_key].remove(letter)
            num_count.setdefault((num_count_key + 1), []).append(letter)
            char_count[letter] += 1
        i += 1

    max_val = sorted(num_count.keys())[-1]

    return sorted(num_count[max_val])

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
