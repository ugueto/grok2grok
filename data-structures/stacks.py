"""
    Stacks are linear data structures, that store and process data in a
    Last-In-First-Out (LIFO) manner.

    Think of it as a stack of dinner plates when setting a table,
    you remove the topmost plate first, on and on, until there are none left.

    Stacks have 3 basic operations:
        - Push: Adds an object to the top of the stack.
        - Pop: Removes an object from the top of the stack.
        - Peek: Check, without removing, the object at the top of the stack.
    
    Whenever we attempt to push an object to a full stack, this will cause Stack Overflow.
    Whenever we attempt to pop an object from an empty stack, this will cause Stack Underflow.

    Stacks are easily implemented in Python using lists.
        - Push = list.append(item)
        - Pop = list.pop()
        - Peek = print(list[-1])
"""

class Stack:
    def __init__(self):
        self.items = []
    
    # We could add a method to check if the list is empty
    # Thus avoiding Stack Underflow when using add / push.
    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        return self.items
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is currently empty.")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is currently empty.")

    # Checking the size could also be useful. Technically, we can't have an infinite stack, so we limit it.
    # We could add an is_full method and we could add a maxsize attribute.
    def size(self):
        return len(self.items)

sample_stack = Stack()
# Imagine we are taking plates out of the dishwasher.
# We are making a stack of plates.
sample_stack.push("First plate")
sample_stack.push("Second plate")
sample_stack.push("Third plate")

# Then we need those plates to set the table.
sample_stack.pop()
sample_stack.pop()
sample_stack.pop()

# Is there anything to peek?
sample_stack.peek()


"""
    As you have likely deduced, this is an interpretation of a Stack,
    but it is an unnecessary one.

    We can just create a list called stack and use .pop() and .append()
    But, as lists grow, we can run into some problems...
    A list may be familiar, but it should be avoided because it can potentially have memory reallocation issues.
    As seen in queues.py, for Stacks we could also use two built-in alternatives:

    - collections.deque using .append() and .pop() - faster than lists as the stack grows!
    - queue.LifoQueue which is a Last-In First-Out queue! In this case you use .put() and .get() - safer for threading!

    Both are useful for certain scenarios, but keep this in mind:
        - Stacks do not provide fast access to elements other than the top element.
        - Stacks do not support efficient searching (although this is uncommon in Stacks), 
        as you have to pop elements one by one until you find the element you are looking for.
"""
