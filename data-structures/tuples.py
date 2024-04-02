"""
    Tuples are a useful, built-in Python data type / structure.
    They are closely related to lists (they are sequences as well: https://docs.python.org/3/library/stdtypes.html#typesseq).
    But they have something else that makes them unique.

    Tuples are ordered but also UNCHANGEABLE, or immutable as you prefer.
    This means there is no append or pop method to add/remove values.

    They follow the same indexing as lists, and allow duplicate values.
"""
# Instead of brackets, they are created in between parenthesis.
sample_tuple = ("one", "two", "three")  # Creating tuples is also called packing!

print(len(sample_tuple))  # We also have a len() method for the length of the data structure.

# An interesting edge case:
# When you create a tuple with one object, it must have a comma afterwards.
# Else it will not recognize it as a tuple.
empty_tuple = ()  # It has zero items inside, and none can be added.
is_not_a_tuple = ("wrong!")
is_a_tuple = ("right!",)  # Try printing the data type of both these variables :)
also_is_a_tuple = "right", # Crazy, right? This works also! Try printing the data type of these variables.

# Like lists, they accept multiple data types and can be indexed (starting from 0).
another_tuple = ("one", 1, False, "two", 2, True)
print(another_tuple[0])
print(another_tuple[-1])

# Another way to build them is using the tuple() constructor, but this can be redundant.
one_more_tuple = tuple(("some data", "more data"))

# Slicing a tuple is the same as lists
tup_tup = (1, 2, 3, 4, 5)
print(tup_tup[1:4])

# Remember I mentioned packing? Well, there is also unpacking!
# We can extract the values of a tuple, without changing it, and assigning them to variables.
# Take a good look into the syntax!

unpackable_tuple = (1, 2, 3)
(one, two, three) = unpackable_tuple  # This might prove useful for extracting values!

print(one)
print(two)

# Although there are no add / remove / update methods.
# We can use .count() and .index() the same way we have them in lists.

print(unpackable_tuple.count(1))
print(unpackable_tuple.index(2))  # Remember, this returns the index of the FIRST occurrance of a value!
