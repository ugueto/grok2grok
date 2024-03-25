"""
    Queues are linear data structures, that store and process data in a
    First-In-First-Out (FIFO) manner.

    Think of a real queue, maybe at a supermarket cashier.
    The first person to reach the cashier to pay, is the first one to exit.
    Then the second person becomes the first in line, and so on.
    The last person to join will be the last one to pay for their groceries.

    There are multiple ways to do queues in Python, we will create a few here.
    - using collections.deque (pronounced deck).
    - using queue.Queue
    - using a list (as mentioned in arrays.py, this is a slow approach!)

    A few concepts we need to know first are:

    Enqueue: Adding an object to the queue (back of the line!).
    Dequeue: Removing an object from the queue (you're first!).
"""

from collections import deque
from queue import Queue

# FIRST OPTION: Lists
# Let's start with the "worst" approac: a list / array.
supermarket_queue = []

supermarket_queue.append("First customer")  # Cashier opens, a first customer gets to the line, we add them to the queue.
supermarket_queue.append("Second customer")  # .append() is useful because it adds customer to the back of the line.
supermarket_queue.append("Third customer")

# In order to dequeue, we could use .pop(0) which removes the first item of a list.
# This is where thins slow down, if we do this, all remaining items have to move one index to the left.
# e.g Second customer would move to position #1, the Third customer to position #2, etc.  

supermarket_queue.pop(0)  # The first customer has already paid - let's remove him.

# Using lists: append is O(1) runtime but pop(0) would be O(n) runtime, slowing us down!

# SECOND OPTION: collections.deque
# A better and faster approach would be using collections.deque
# This allows us to have O(1) runtime for both append and pop.
# In this case, deque has two useful methos, appropiately called: append() and popleft()

transport_queue = deque()
transport_queue.append("First transport rider")
transport_queue.append("Second transport rider")
transport_queue.append("Third transport rider")  # Let's assume this is a small vehicle for transport that only has 3 seats.
print(transport_queue)

# Now it transport has arrived, time for people to get off the bus.
transport_queue.popleft()
transport_queue.popleft()
transport_queue.popleft()

# NOTE: If we attempt to .popleft() when a Queue is empty, we would get an IndexError.
print(transport_queue)

# THIRD OPTION: queue.Queue
# Python has its own built-in queue module which allows us to implement queues.
# A good thing about queue.Queue is that it allows us to specify the maximum size.

infinite_queue = Queue(maxsize=0)  # If we set maxsize equal to 0, the default, then there is no maximum size!

# In order to add new items we use .put()
infinite_queue.put("Number one")

finite_queue = Queue(maxsize=2)

# We can check if the queue is empty using .empty()
# This is useful to avoid errors when attempting to Dequeue an item.
print(finite_queue.empty())

# Fortunately, .put waits for a space to open up if the queue is full.
# If you want an immediate operation that if the queue is full, returns an error.
# We can use .put_nowait()

finite_queue.put("Number one")
finite_queue.put("Number two")
# finite_queue.put_nowait("Number three is one too many!") - this would raise a QueueFull error.

# We can check if the queue is full e.g. size = maxsize! - To get size you can use .qsize()
# This is useful to avoid errors when attempting to Enqueue an item.
# if maxsize is set to 0, then full will NEVER return True.
print(infinite_queue.full())
print(finite_queue.full())
print(f"{finite_queue.qsize()} is equal to maxsize!")

# For retrieval, we use .get() and .get_nowait()
finite_queue.get()
finite_queue.get_nowait()
finite_queue.get()  # This last call will wait for a new valuable to be added to finite_queue.


"""
    Another useful tip when using the queue built-in module:
        1. LifoQueue - creates a Last-In First-Out queue.
        2. PriorityQueue - creates a Queue with prioritized items.

    Read more on: https://docs.python.org/3/library/queue.html
"""
