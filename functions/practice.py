"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    """Prints 'Hello World'"""

    print "Hello World"

# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    """Takes in a name as a parameter and prints a message saying 'Hi' to that name"""

    print "Hi", name


# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.

def print_product(integer_1, integer_2):
    """Takes in two integers as parameters and prints the product of their multiplication"""

    print integer_1 * integer_2

# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times

def repeat_string(string, integer):
    """Takes in a string and an integer as parameters and prints the string as many times as the integer"""

    print string * integer

# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".

def print_sign(integer):
    """Takes in an integer as a parameter and prints if it is higher or lower than zero, or the number zero itself"""
    
    if integer > 0:
        print "Higher than 0"
    if integer < 0: 
        print "Lower than 0"
    if integer == 0:
        print "Zero"

# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def is_divisible_by_three(integer):
    """Takes in an integer as a parameter and returns a boolean indicating if the integer is evenly divisible by 3"""
    
    if integer % 3 == 0:
        return True
    else:
        return False

# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.

def num_spaces(sentence_string):
    """Takes in a string of a sentence as a parameter and counts/returns the number of spaces in the string"""
    
    space_count = 0

    for character in sentence_string:
        if character == " ":
            space_count = space_count + 1

    return space_count


# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_meal_price(meal_price, tip_percentage = .15):
    """Takes in meal price before tip as a parameter and tip percentage as an optional parameter (which defaults to 15%), returns total meal price."""

    total_price = meal_price + (meal_price * tip_percentage)

    return total_price

# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.

def sign_and_parity(integer):
    """Takes in an integer as a parameter and returns a list that indicates if that integer is positive or negative and even or odd."""

    num_info = []

    #I recognize that this might be simpler looking if it had if/else statements but I don't want my function 
    #to call 0 positive/negative 

    if integer % 2 == 0 and integer:
        num_info.append("Even")
    else:
        num_info.append("Odd")
    if integer > 0:
        num_info.append("Positive")
    if integer < 0:
        num_info.append("Negative")

    return num_info

sign = sign_and_parity(5)[1]
parity = sign_and_parity(5)[0]

print sign, parity 

################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

def full_title(name, job_title = "Engineer"):
    """Takes in a name as a parameter and a job title as an optional parameter (defaults to engineer). Returns a full title (Job and Name)"""
    
    return job_title + " " + name


# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def write_letter(recipient_name, job_title, sender_name):
    """Takes in a recipent name, job title and sender name to print a generic message."""
    
    print "Dear " + full_title(recipient_name, job_title) + ", I think you are amazing! Sincerely, " + sender_name


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
