"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """

    for item in items:
        print item


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """

    long_words = [word for word in words if len(word) > 4]

    return long_words

def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    n_long_words = [word for word in words if len(word) > n]

    return n_long_words


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """

    numbers.sort()

    if len(numbers) == 0:
        return None
    else:
        return numbers[0]


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """

    numbers.sort()

    if len(numbers) == 0:
        return None
    else:
        return numbers[-1]


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

    halvesies = [float(number)/2 for number in numbers]

    return halvesies


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """

    word_lengths = [len(word) for word in words]

    return word_lengths


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """

    # if len(numbers) == 0:
    #     return 0  
    # ^ wrote this and then realized I really didn't need it/code is superfluous because this already happens

    sum_num = 0
    for number in numbers:
        sum_num = sum_num + number

    return sum_num


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """

    product = 1 

    for number in numbers:
        product = product * number

    return product


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """

    joined_string = ''

    for word in words:
        joined_string = joined_string + word

    return joined_string


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    sum_nums = 0

    for number in numbers:
        sum_nums = sum_nums + number

    average = float(sum_nums) / float(len(numbers))

    return average

def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    joined_string = ""

    for word in words:
        if len(words) == 1:
            joined_string = word
        elif words[0] == word:
            joined_string = joined_string + "" + word + ", "
        elif words[-1] == word:
            joined_string = joined_string + "" + word
        else:
            joined_string = joined_string + "" + word + ", "

    return joined_string


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    reversed_list = []

    for i in range(len(items)):
        i = i + 1
        reversed_list.append(items[-i])

    return reversed_list


def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """

    #I knew it would be pretty easy to solve this by doing what I did above and just adding a step where I 
    #save the new list as the old list's name, but I figured that was probably not what you wanted me to do.
    #I ended up with this kind of funky code, but it works? I think there is maybe a better way, but this was the 
    #solution that I found that worked with lists of different lengths (not just lists of len(3))

    length = range(len(items))

    length.sort(reverse = True)

    for i in length:
        items.append(items[i])

    to_delete = len(items) / 2 
    range_to_delete = range(to_delete)

    range_to_delete.sort(reverse = True)

    for i in range_to_delete:
        items.pop(i)


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """

    duplicates_list = []

    for i in range(len(items)):
        for x in range(len(items)):
            if i != x and items[i] == items[x]:
                if items[i] not in duplicates_list:
                    duplicates_list.append(items[i])

    return duplicates_list
    
    #the below version of code is easier to follow in my opinion, but alas does not return in ascending order
    # duplicates_list = []
    # reference_list = []

    # for item in items:
    #     if item in duplicates_list:
    #         pass
    #     elif item in reference_list:
    #         duplicates_list.append(item)
    #     else:
    #         reference_list.append(item)

    # return duplicates_list


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """
    indices_list = []
    
    #I think there might be a better way to do what I'm doing below, but when I didn't set the default to 
    #"None" before I iterated through the list, I kept accidentally setting all of the values in the 
    #indices list to "None"
    for z in range(len(words)):
        indices_list.append(None)

    for i in range(len(words)):
        for x in range(len(words[i])):
            if words[i][x] == letter:
                indices_list[i] = x
                break

    return indices_list


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
