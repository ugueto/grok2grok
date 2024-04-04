"""
    A primer on Python decorators!

    What are decorators?
    Put simply, a decorator (usually) wraps a function, modifying its behaviour.
    But remember, a decorator is just a regular Python function that takes in a function as argument.
    It can do many sorts of things with that function:
        - Run it
        - Perform an action with its arguments
        - Perform an action with its return value
        - Extend the function
        - Call it once, twice, thrice...
        - Do actions before and/or after running the function.

    A simple debugger decorator could be:
        a. prints function name
        b. prints arguments
        c. THEN RUNS THE FUNCTION.
        d. prints return value
        e. prints runtime

    Essentially,  it allows programmers to modify the behaviour of a function or class*
    *(On classes later on, for now focus on functions and methods).
    This is both useful and powerful stuff!

    Note: It would be useful to fully understand first-class objects and inner functions!
        - In short, functions are first-class objects and can be passed as arguments to other functions
            *Without calling them, but referencing them (e.g. not function_name() but function_name)

    For more simple, real life examples see: https://realpython.com/primer-on-python-decorators/
    For further details see: https://wiki.python.org/moin/PythonDecoratorLibraryclear
"""

import functools

# This is a simple decorator function.
# It will just run the function named func twice inside the inner wrapper function.
def decorator(func):
    def wrapper(*args, **kwargs):
        # This wrapper returns nothing, so func will be run twice, but return/store nothing.
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper  # Notice we are not CALLING the wrapper function, but referencing it.

@decorator
def example():
    print("This is an example.")
    return "Cannot store it as wrapper has no return statement!"

example()  # I can't store any value returned from this.

i_cannot_store_this = example()
print(i_cannot_store_this)  # > None

def another_decorator(func):
    @functools.wraps(func)  # functools.wraps helps decorated functions point to themselves, instead of the wrapper.
    def another_wrapper(*args, **kwargs):
        # This inner wrapper function returns func and stores it's return value.
        return func(*args, **kwargs)
    return another_wrapper

@another_decorator
def another_example():
    print("This is another example.")
    return "You can store this!"

i_can_store_this = another_example()
print(i_can_store_this)  # > "You can store this!"


# DECORATOR SAMPLE FORMULA

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # You can do something before or after calling/returning func.
        return func(*args, **kwargs)
    return wrapper  # Remember to skip the parenthesis.

@decorator
def sample_func():
    return 1


"""
    More advanced topics:
        1. Decorating classes.
        2. Using multiple decorators.
        3. Decorators with arguments.
        4. Stateful decorators.
        5. Classes that act as decorators.
"""
