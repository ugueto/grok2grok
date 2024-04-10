"""
    What are Lambda functions (or Lambda expressions)?

    In short, a Lambda function is a small, anonymous function (synonym is actually anonymous function).
    But, what does that even mean?

    There are 3 basic distinctions from regular functions and Lambda:
        1. Syntactic sugar.
        2. They are concise, which saves memory and speeds performance.
        3. They are (loosely) anonymous.

    It is also worth noting, looking cleaner does not always mean it helps readability!

    Now, be careful: Lambdas should NOT replace regular functions.
    The examples you usually see, does not mean they are better alternatives to a def function.

    The real use case would be: one (or two) uses, handy, throw-away functions.

    Response from a CPython core developer:

    "If you're going to reuse a function more than once, use def - that's what it's for, for the reasons above. 
    The whole intention of a lambdas (again, aka anonymous functions) are for throwaway,
    use-once functions that you don't want to bother giving a name, because you're not going to use them again."

    From Python Design and History:

    "Unlike lambda forms in other languages, where they add functionality,
    Python lambdas are only a shorthand notation if you're too lazy to define a function."

    Further notes: 
    They are considered "anonymous", so Exceptions with lambdas can be harder to trace.
    Python identifies them as <lambda> where as regular functions are identifiable.
    They can't contain statements, only a return expression.
    They are ONE-LINER functions, you can extend to multiple lines but this is highly discouraged.
    They do not support type annotations.
    They support the use of decorators.
    They accept *args, **kwargs, and argument assigning.

    For more details see: https://realpython.com/python-lambda/

    Now that we know all this, let's give them a try!
"""

# Syntax: lambda arguments: expression
# You should ideally not assign lambda functions, below is just an example.

l_func = lambda x: x + 1  # noqa: E731 - don't mind this, it just eliminates style errors :)

# The lambda function above takes an argument x, and then adds x + 1
# As you'll see below, we can run them using the same syntax as regular functions: lambda_name(arguments)
print(l_func(1))

# We can also run them without a name, immediately. Although this is discouraged.
print((lambda x: x + 1)(1))

# Lambda expressions can have multiple arguments:
another_l_func = lambda a, b: a * b  # noqa: E731
print(another_l_func(2,3))  # returns 2 * 3

# Lambda expressions can have functions as arguments!
one_more_l_func = lambda y, func: y + func(y)  # noqa: E731

def sample_function(y):
    return y + 1

# With a regular sample function
print(one_more_l_func(1, sample_function))  # What does this return?

# With another lambda expression
print(one_more_l_func(1, lambda x: x * x))  # What does this return?
