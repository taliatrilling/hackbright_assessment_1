# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def total_item_cost(state, cost_before_tax, tax = .05):
	"""Determines the total cost of an item with tax included

	Takes in as parameters in the state where the item is being purchased, the cost of 
	the item before the tax is added, and a tax rate, which if not specified,
	defaults to 5%. Additionally, if the state is specified to be California (state 
	abbreviation = CA), a 7% tax will automatically be applied."""

	if state == "CA":
		tax = .07
	
	total_cost = cost_before_tax + (cost_before_tax * tax)

	return total_cost


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit_name):
	"""Takes in a fruit name as a parameter and checks if it is a strawberry, cherry or blackberry

	References an established list of berries and returns a boolean to indicate if the fruit passed in 
	is one of those berries"""

	berries = ["strawberry", "cherry", "blackberry"]

	if fruit_name in berries:
		return True
	else:
		return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit_name):
	"""Takes in a fruit name as a parameter, uses it to call is_berry, and calculates shipping cost based on whether or not it is a berry."""

	if is_berry(fruit_name):
		return 0
	else:
		return 5

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town_name):
	"""Takes in a town name, returns True if town is Washington D.C. (my hometown), and false if it is not.

	Attempted to account for the various ways to represent D.C. since it is kind of uniquely known a few ways,
	as well as capitalization choices."""

	DC = ["washington d.c.", "dc", "washington dc", "d.c."]

	if town_name.lower() in DC:
		return True
	else: 
		return False
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first_name, last_name):
	"""Takes in a first name and a last name as two parameters, and returns a concatenated string of the full name."""
	
	return first_name + " " + last_name

#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(hometown, first_name, last_name):
	"""Takes in a hometown, first name, and last name as parameters, calls existing functions is_hometown and
	full_name and prints a message dependent on whether the hometown matches mine."""

	if is_hometown(hometown):
		print "Hi " + full_name(first_name, last_name) + ", we're from the same place!"
	else:
		print "Hi " + full_name(first_name, last_name) + ", where are you from?"

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x = 1):
	"""Function (taking an integer as an optional parameter that defaults to 1) 
	with a nested function requiring another integer to be called, that adds two values."""

	def add(y):
		return x + y
	return add
		

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

addfive = increment(x = 5)

addfive(y = 5)

addfive(y = 20)


# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def number_list(number, existing_number_list):
	"""Takes in a number and a list of numbers as parameters, appends the number to the existing list
	and returns the list of numbers (which now includes the number taken in)"""

	existing_number_list.append(number)
	return existing_number_list


#####################################################################

