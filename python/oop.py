"""
    Object-Oriented Programming, OOP for short, is fundamental in Python.

    Why? Well, Python is considered an object-oriented programming language (for the most part).

    What does this mean?
    OOP is simply used to model real life through objects and classes.

    Classes are the blueprints of objects. (For example, a Blueprint of a Car model.)
    Objects in this Class have attributes (properties: values / variables / data structures) and behaviors (functions / methods!).

    For example:

    In a real-world scenario, you have birds (we can model this as a Class named Birds).
    Birds have attributes: color, size, age, maybe even a name.
    Birds can have behaviors: when they make a dance, a sound, or their song, for example.

    Once we create an object from this class, we call it an *instance*.
    Lastly, to this instance we add an identity, or unique name, and assign it to a variable.

    OOP also helps write re-usable, efficient, code. Instead of repeating ourselves for every object, we have a shared blueprint.

    OOP also introduces an important subject named *Inheritance*.

    Inheritance is a way to represent a hierarchy of classes that share or derive traits and behaviors.

    A simple example could be:
    Birds, could inherit from the class Animals. They would be referred to as a Subclass (or Child) of Animals (Parent).
    If we go a step deeper, we could create a Subclass of Birds called Crows.

    And the inheritance hierarchy would look like this: 
    "A Crow is a type of Bird, which in turn is a type of Animal."

    You may find some examples of this object modeling in Python below:
"""


class Bird:
    # Classes can have class attributes, meaning they are shared by all class objects.
    # All Birds are vertebrates, but not all birds have the same name!
    animal_type = "vertebrate"

    # __init__ the initializer method is also called the constructor or instantiation method. Used for creating objects.
    # Both class and self are OOP keywords in Python, more on this in keywords.py
    def __init__(self, name: str, color: str, age: int = 0):
        self.name = name
        self.color = color
        self.age = age
        self.dance = False
        self.sing = False

    # __str__ is a representational method for the class, to display objects in a String.
    def __str__(self):
        return f"{self.name} is a bird, colored {self.color} and {self.age} years old."
    
    # Another important subject is: Getter and Setter methods, used to get or set attributes in an object.
    # Below you can see examples to get or set the name of the bird, but they can be created for any attribute.
    def get_name(self):
        return self.name
    
    def set_name(self, new_name: str):
        self.name = new_name

    # We can also use methods to represent behaviors in objects.
    # For example, if the bird sings, we can attempt to simulate their song (imagine they all share same song).
    def sing(self):
        if self.sing:
            print("Shalalala bird song!")
        else:
            print("This bird is not a singer!")

# Sample instance
# Notice we don't assign age as it has a default value of 0 (Larry is a newborn!)
larry_bird = Bird(name="Larry", color="green")

# We can fetch attributes via the .attr notation or getter methods.
print(larry_bird.name)
print(larry_bird.get_name()) # Both these lines return the same string.

# We can also assign or change attributes with setter methods.
larry_bird.set_name(new_name="Larrius")  # He wanted his birth name!

"""
    Two more fundamental subjects in OOP are: Polymorphism and Encapsulation

    Polymorphism means, in short, one thing can take many forms.

    For example, many birds dance and sing - now *how* they perform this changes by Bird class.
    A robin does not sing like a nightingale. Hence, they both have the method .sing() but return different results.

    Encapsulation means the process of wrapping up variables and methods into a single entity.
    This way, we can add restrictions to attributes and behaviors of objects.

    You can have: public, private, and protected accessibility.
    Public are accessible anywhere.
    Protected are accessible within the class and it's subclasses, it is noted by an underscore prefix.
    Private only accessible within the class, and noted by a double underscore prefix.

    This makes code more readable and secure, at least for programmers to know.
    See example below:
"""

class BankAccount:

    def __init__(self, owner: str, id: int, money: int = 0):
        self.owner = owner  # Owner of the bank account is a public attribute.
        self._id = id  # The ID number of owner is a protected attribute.
        self.__money = money  # The amount of money in the bank account is a private attribute.


"""
    One final subject to learn about OOP is: Abstraction
"""
