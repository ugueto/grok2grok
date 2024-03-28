"""
    What are functions?

    Functions are blocks of code which perform an intended action and are re-usable.
    You can use Python's built-in functions (see common_methods.py) or create your own.
    Or you can also check out lambda functions in lambda.py

    Imagine a mathematical function: f(x) = x + 1

    Hope this is not too boring but functions in Python are an interpretation of the above.

    For any given value of `x`, we will add 1 -> x can be 1, 2, 3 -3, 100, whatever!

    Python functions are similar: we define a set of statements, that sometimes take
    arguments (x in the example above), and with those arguments we then perform actions.

    This is a convenient way to organize and re-use blocks of code!

    Let's see an example.
"""

def example_function():
    """
        A few things to note here:
            1. We use to keyword def (short for define) to begin a function statement.
            2. Function names are (according to PEP8 - see pep8.py) written in snake_case.
            3. We then add the parenthesis which includes all arguments, in this particular case, we have no arguments!
            4. If necessary, adding code blocks (Docstrings) like these one could be useful for other developers.
    """
    # The keyword pass does nothing - it is just a placeholder.
    pass

def sum_one(x: int):
    """
        Remember that boring mathematical function I wrote above?
        Here it is in Python, and we added a few things!

        1. This function has a verbose name - write good, self-explanatory code!
        2. It takes an argument named `x` which is an integer (we can't add 1 to a string!)
        3. There is a new keyword, return, which is added to return the result of a function.
            When called, the return keyword finalizes the run of the function.
    """
    return x + 1

def multiple_returns(x: int) -> str:
    """
        Two new things to note here:
        1. As you'll see below, one function can have multiple return statements.
            Depending on the parameter* we provided - we get a different string.
                * -> parameter is written at the function declaration.
                  -> argument is the data or information passed into the function.

        2. We added a type hint to the return statement!
            After the parenthesis we added "-> type" which claims this function
            returns an object of the type `str`.
    """
    if x > 1:
        return "This is greater than 1"
    elif x == 0:
        return "0 is a cool number"
    else:
        return "What a negative nellie!"


# To call a function, we just write it again without def

example_function()  # This one does nothing


sum_one(1)  # Will this line of code actually print anything? 

# Well, no it didn't. We need to use it or store it.
print(sum_one(1))
equals_three = sum_one(2)
print(equals_three)
print(multiple_returns(0))

def sum_xyz(x: int, y: int, z: int) -> int:
    # We can also add as many arguments as we want.
    return x + y + z

# We can also specify arguments when calling the function.
sum_xyz(x=1, y=2, z=3)

# You can also check kwargs.py for *args and **kwargs!

def has_a_default(x: int = 0) -> int:
    # Imagine you forgot to add a value, well we can add a default after the argument!
    return x + 1

print(has_a_default())  # Will it run or get an error?

def accepts_an_iterable(values):
    """
        Two things to note here:
            1. This function accepts any iterable* object (e.g. List, String, etc)
                * This is bad code - we don't specify what type and it can easily break. Just an example.
            2. It doesn't have a return statement! It is not needed.
    """
    for value in values:
        print(value)
