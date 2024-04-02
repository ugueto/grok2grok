"""
    Sets are one of the 4 built-in data types / structures in Python.

    What makes them unique? When are they useful?

    They are, essentially, an opposite of lists and tuples (or sequence types).
    A set is an unordered collection with no duplicate elements.
    They attempt to represent a mathematical sets (how fun!), from set theory.

    Sets can be modified (e.g. add / remove values), but the values inside it cannot be modified.

    See more examples below:
"""

# Creating a set
first_set = set([1, 2, 3])  # We can use the set() constructor with an iterable value.
second_set = {1, 2, 3}  # Looks familiar, no? Yep, like dicts, they also use curly brackets! But not key, value pairs.

# Be careful when using set for iterables, it can be confusing!

iterable_string_set = set("foo")
one_string__inside_set = {"foo"}  # Why are these different? Try printing them!

# Empty sets can't be created with empty curly brackets, this is for dicts!
# We must use set()
empty_dict = {}
empty_set = set()

# Sets, like other built-in data structures, accept multiple data types.
sample_set = {1, False, "Juan", 3.0}

# Since lists and dicts are mutable, they cannot be inside sets!
# Try running: set([1, 2, 3]) and see for yourself.

# We can also use len() for sets
print(len(sample_set))

"""
    Here's the cool part about sets.
    You can use most mathematical set theory operations on them.

    Such as union, subsets, intersection, etc.
"""

# Set union - there are 2 ways:
set_one = {1, 2, 3}
set_two = {4, 5, 6}

united_set = set_one | set_two  # The difference is with | we need both elements to be sets.
another_united_set = set_one.union(set_two)  # With .union() the second elem can be any iterable.

# Also, union accepts multiple arguments while | can be repeated.
sample_string = "abc"
sample_list = [1, 2, 3]
sample_set = {3, 4, 5}

big_set = sample_set.union(sample_string, sample_list)  # Both a string and a list are iterables.
bigger_set = set_one | set_two | big_set

# In all the below operations we can also specify multiple objects, but they might follow different processes.
# Set intersection
print(set_one & bigger_set)
print(set_one.intersection(bigger_set))  # All elements in set_one that are in bigger_set as well.

# Set difference
print(bigger_set - big_set)
print(bigger_set.difference(big_set))  # All elements from bigger_set once you eliminate any elements from big_set

# Symmetric difference - 
print(bigger_set ^ big_set)
print(bigger_set.symmetric_difference(big_set))  # All elements in bigger_set and big_set but NOT in both.

# is_disjoint
print(big_set.isdisjoint(bigger_set))  # Checks if big_set has any elements in common with bigger_set
# If they have NO elements in common, it will return True, else False.
# In other words, if True, their intersection would be an empty set.

# is_subset
print(big_set.issubset(bigger_set))  # Returns True if all elements in big_set are also in bigger_set
print(big_set <= bigger_set)

# Two edge cases to note in subsets!
# An empty subset is always a subset.
# The same subset is always a subset.
print(big_set <= big_set)
print(set() <= big_set)

# For proper subsets we use just < symbol
# Proper subsets mean A & B can't be equal, but all elements in A appear in B. Hence A is proper subset of B.

print(big_set < bigger_set)

# is_superset
# Supersets are the reverse of subsets!
# e.g. All elements in A appear in B. A is a superset of B.
print(bigger_set >= big_set)
print(bigger_set.issuperset(big_set))

# Just like before, a proper superset means object is a superset but they can't be equal!
print(bigger_set > big_set)

# MODIFYING A SET
# Each of the operations used above can be augmented to alter a set.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)  # .update() adds the union into set1
set1 |= set2  # |= is the equivalent operator to update

set2.intersection_update(set1)  # .intersection_update() adds the intersection into set2
set2 &= set1  # &= is the equivalent operator to intersection update

set1.difference_update(set2)  # .difference_update() adds the difference into set1
set1 -= set2  # -= is the equivalent operator to difference update

set1.symmetric_difference_update(set2)  # .symmetric_difference_update() adds the symmetric_difference into set1
set1 ^= set2  # ^= is the equivalent operator to symmetric difference update

# Adding elements
one_more_set = {1, 2, 3}
one_more_set.add(4)

# Removing elements
one_more_set.remove(3)  # If 3 were not in the set, this would raise an Exception!

# Carefully removing elements! Useful
one_more_set.discard(5)  # If 5 is present, it will remove the element. If not, it does nothing.

# A different pop!
one_more_set.pop()  # .pop() removes and returns a random element of the set, if set is empty it raises an Exception.

# Clear a set
one_more_set.clear()  # Removes all elements from a set


"""
    One last thing!

    There is another built-in data type called frozenset, that,
    is almost exactly the same as a set BUT...

    They are immutable!

    Hence you cannot add, remove, pop, clear, or modify in any way.

    NOTE: Augmented assignments (|=, &=, -=, ^=) like the ones seen above CAN be used in frozensets,
    essentially "modifying" the original frozenset, but not really. 
    Augmented assignment does not modify a set, it replaces it with a new one!
    The original frozenset will no longer be stored in memory and be replaced with a new id.
"""

its_freezing = frozenset([1, 2, 3, 4])
print(len(its_freezing))
