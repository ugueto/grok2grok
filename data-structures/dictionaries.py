"""
    Is it a dictionary or a HashMap?
    SAME THING!

    Dictionaries are data structures that hold information in key:value pairs.

    Imagine a real life dictionary, it follows the structure word:meaning.

    In order to find the value in a HashMap, or dict, you use its key.
    Dictionaries are faster than lists when searching, but take more space.

    For example, when you want to look in a dictionary for a word (Oracle), 
    you don't start from the letter A and go page by page, you jump to the letter O,
    then maybe to O followed by R, and so on.

    This is a "similar" approach to a Binary Search algorithm, if you're already familiar.

    dicts:
    - are ordered* (from Python 3.7+)
    - are mutable (you can change, add, and delete items continuously)
    - do not allow duplicate (keys)
        *You can't have the same keys (it will be overwritten), but two keys can have the same value.
        *Due to this, keys must be immutable data types, unlike values.

    Keys and values can be multiple data types:

"""

# dicts are created with curly brackets, and have key:value pairs separated by commas. 
example_dict = {
    "apple": "a fruit",
    "car": "a machine",
    "human": "an animal"
}

# An alternative method is using .dict(key = value, key2 = value2)

# Similar to lists, we can find out how many items are in a dict with len()
print(len(example_dict))

# There are many ways to retrieve information from dictionaries
# using a key

print(example_dict["apple"])  # prints the value! Not the dict, or the key.

# But what if you don't know if the key exists already?
# Say for example, you have some grades to an exam (on a scale of 10).

grades_dict = {
    "Paula": 10,
    "Ana": 8,
    "Ryan": 3,
    "Lisa": 7,
    "John": 9
}

# We forgot Charlie was sick and still tried to fetch his grade:
# print(grades_dict["Charlie"])

# The above command will raise an error! For these scenarios, it is safer and more reliable to use .get()
print(grades_dict.get("Charlie"))  # If the key is not found, .get() returns a default value of None.
print(grades_dict.get("Charlie", "Hey, Charlie is not in here!"))  # We can override the default return value!

# If you just want to check if the key exists - not fetch the value. We use the in keyword.
print("Alex" in grades_dict)

# We can also fetch:
# - All items using dict.items(), as tuple (key, value) pairs in a list.
# - All keys using dict.keys()
# - All values using dict.values()

print(grades_dict.keys())
print(grades_dict.items())

# In order to append or change existing values, we can use dict[key] = value format.
grades_dict["Charlie"] = 10  # Charlie presented on another day.
grades_dict["Ana"] = 7  # Ana lost 3 points due to cheating!

# We could also use the .update() method
grades_dict.update({"Lisa": 10})
grades_dict.update({"Peter": 6})

# Another neat trick of update, you can append two dictionaries together using dict_1.update(dict2)

# In order to remove existing key, values we use either .pop() method or the del keyword.
grades_dict.pop("Lisa")
del grades_dict["Ana"]  # CAREFUL! Remember to add the key, if not you could delete the whole dict.

# If we want to empty the dict, we can use .clear()
example_dict.clear()

# There exist nested lists, how about nested dictionaries? Sure!
customers_dict = {
    "customer_1": {
        "first_name": "Oscar",
        "last_name": "Dean",
        "id": 1
    },
    "customer_2": {
        "first_name": "Lucas",
        "last_name": "Perez",
        "id": 2
    },
    "customer_three": {
        "first_name": "Rachel",
        "last_name": "Potter",
        "id": 3
    }
}
