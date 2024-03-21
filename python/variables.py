"""
In order to start, we need to take the first step,
and when learning Python, that step is: VARIABLES.

What is a variable?
- In short, a variable is an container/pointer that stores (or points to, duh!) some form of data/object.
- This "variable" we have created will point to that data in memory.
- It is the basic unit of data storage in Python.

Python is dynamically-typed (not statically-typed like other programming languages), so variables can point
to different data types or be re-declared to point to another data type.

What type of data can be stored in variables?
- Python has many different data types, see below:
"""

variable_one = 1  # int (integers or whole numbers)
variable_two = 1.0  # float (floating point numbers or decimals)

variable_three = "My name is Juan"  # string (text)
variable_four = 'My name is also Juan'  # Can you spot the difference? Both single and double quotes work.

variable_five = True  # bool (boolean or True/False)
variable_six = False  # Also a boolean :)

"""
All 3 variables store different data with different data types.
We can now use this data, in any way we wish.

Variables in Python usually follow the snake_case naming convention (lower case separated by underscores).
They also start with letters, not numbers, and are case-sensitive.

One exception are constant variables, e.g. a variable that won't change, this go in ALL_CAPS.
"""

VALUE_OF_PI = 3.14  # It will always be 3.14!

variable_one = 2
variable_two = variable_three  # As you can see, variables can be re-written (so be careful!).

print(variable_one)
print(variable_two)  # What do you think will appear in the console?

# You can also assign the same value to multiple variables, see below:

x = y = z = "Same value!"

# Or you can assign them to different values in the same line but separated by commas.
# None of these statements are very readable, so avoid them!

a, b, c = 1, 2.0, "Crappy code!"

"""
Another important concept to be seen is:
    - Variables can be LOCAL or GLOBAL, depending on where they are declared.

    More on this later own.
"""
