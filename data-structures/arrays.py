""" You mean lists, right?!

Arrays (lists henceforth) are mutable, ordered collections of data.
As a variable pointed to an object, data structures such as lists can store many variables/objects!

They are one of 4 built-in data structures in Python, and have many useful built-in methods.
Also, they are one of the most common, simple data structures you should learn.

Lists can store any data type, and combine them together in one place. You may also add duplicates.

Imagine a list of athletes, running a Marathon.

Athletes can be taken out (due to injury, for example),
or added in (new runners want to join!). Hence, the list is mutable.

Every athlete has their number (index in Python),
which indicates their position in this list. Hence, the list is indexed.

Note: Lists are indexed from 0 to n. The last item in the list can be fetched with -1 index.

"""

# We can create a list of names (strings!) to store these runners.

runner_list = ["Adam Adams", "John Johnson", "Jacob Jacobs"]

# Let's say we want to find runner #2, we can index the list.

print(runner_list[1])  # Remember index starts at 0 - so runner #2 is at index 1.

# Say for example, you don't know what position Jacob Jacobs is at! Use .index()
runner_list.index("Jacob Jacobs")  # returns 2 - if duplicate, returns index of first instance found.

# How about the last runner to join in?

print(runner_list[-1])

"""
    You can do many things with lists, such as:
        - Add objects (new runners!)
        - Remove objects (lazy guy who never trained and quit...)
        - Replace objects (someone wrote their name wrong)
        - Slice the list (let's say you want to split the marathon by groups)
        - Concatenate lists (you can join your runners with another list from another race)
        - More fun things with indices (reversing the list, getting odd indices only, etc)
        - Sort them (alphabetically, maybe?)
"""

runner_list.append("Jamie Jamieson")  # .append() adds an object to the end of the list.
runner_list.insert(1, "Carlos Gonzalez")  # .insert() accepts an index and an object to add to the list (replacing any current value stored there).

runner_list.pop()  # .pop() removes the object to the end of the list, when passed without arguments.
runner_list.remove("Jamie Jamieson")  # .remove() also removes a given object from the list, if it is duplicated, it removes the first instance.

first_two_runners = runner_list[:2]  # List indexing slices from X to Y (list[X:Y]), X being inclusive and Y excluded.

another_runner_list = ["Sara Daniels", "Lisa Phillips", "Julia Lopez"]
another_runner_list[1] = "List Philips"  # Lisa misspelled her last name, only one L!
all_runners_together = runner_list + another_runner_list  # We can concatenate the lists! You can also use .extend()

reversed_list = all_runners_together[::-1]  # When indexing, the 3rd argument is the STEP of how we want to slice the list. Another method is .reversed()

del reversed_list  # You can use the keyword del if you wish to entirely delete a list.
another_runner_list.clear()  # .clear() removes any objects found inside the list, returning an empty list.

# You can find the length of the list using len()

print(len(all_runners_together)) # Remember index starts at 0 but length at 1. 8 objects = 7 is the last index.

# There are currently 2 common methods used to sort an array/list in Python.
sorted(all_runners_together)
all_runners_together.sort()


# List comprehension helps you create and manipulate lists using loops and conditionals.
runners_with_j = [runner for runner in all_runners_together if "J" in runner]

# If you wish to count the appearances of a value in a list, use .count():
sample_list = [1, 2, 1, 4, 1, 8, 9, 1]
print(sample_list.count(1))


"""
    PRO TIP: 
    Stacks are another data structure we will see later on.
    The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”).
    To add an item to the top of the stack, use append(). 
    To retrieve an item from the top of the stack, use pop() without an explicit index. 
"""


# A list of lists or nested list, can also be used to represent a matrices and tables. See below:

matrix_example = [[1, 1, 1],
                  [2, 2, 2],
                  [3, 3, 3]]

# In this case, you can use multiple indices, to represent the outer list and the inner list.
# Let's say we want the first integer, in the first list.

print(matrix_example[0][0])  # Remember, first = index 0!
