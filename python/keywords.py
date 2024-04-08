"""
    What are Keywords in Python?

    Keywords are just words Python reserves for specific purposes,
    and when I mean reserves it is so nobody uses or overwrites them.

    They are fundamental building blocks of Python's verbose syntax.

    There are, currently (this number changes!), 35 keywords used in Python.
    A great way to learn about these, is using the Python docs.
    Try running help("keywords") in the Python REPL.
    And then try running help("{INSERT-KEYWORD}") for any given keyword.

    If you want to identify them when writing code, most IDEs have syntax highlighting.

    You may find some of them, and its use, below:
"""



""" BOOLEAN KEYWORDS:
    - True
    - False
    - None.
    Note: Always capitalized!

    There are multiple keywords in the example below (def, return, if, etc), but let's focus on the return statements.
    These keywords, True and False, signify boolean values, 0s and 1s, yes or no. Truthy or falsy.
    The "null" keyword in Python is None (capitalized, again).

    You can use bool() to check if certain values are truthy or falsy. Most are truthy.
    Also, values that are considered "null" / no value are classified as False. (e.g. 0, {}, [], "")

    Functions with no return statements automatically return None.
"""

def is_positive_number(num: int):
    if num == 0:
        return None
    elif num > 0:
        return True
    else:
        return False

""" OPERATOR KEYWORDS.
    Operators:
        - and
        - or
        - not
        - is
        - in

    These are meant to represent Math operators and are seen in other programming languages.
"""

# and is meant to return a truthy/falsy value based on two arguments.
# X and Y: True and True = True, True/False and False/True == False, False and False == True.
x = 1 and 1  # = True
y = 1 and 0  # = False
z = x and y  # ???

