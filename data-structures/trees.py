"""
    A tree is a data structure that simulates a hierarchical tree,
    with a root value and the children as the subtrees, represented by a set of linked nodes. 
    The children of each node could be accessed by traversing the tree 
    until the specified value is reached.

    Imagine an actual tree upside down, you begin at the root of the three, and then move
    (traverse) through its branches (edges + internal nodes) until you reach the leaves (end nodes).

    Or imagine a genealogical family tree (but it starts with only one all-mighty ancestor).

    Example: (the arrows are called edges!)
              root
            /      \
        child A    child B
    
    And so on...

    Trees can be considered wide and/or deep.
    Wide = Each node has many children.
    Deep = Many nodes but fewer children per node.

    An important thing to note is, there are many types of trees.
    At least when it comes to naming conventions. For example:

    1. A binary tree is a tree data structure in which each node can have a maximum of 2 children.
        It means that each node in a binary tree can have either one, or two or no children.

    2. A trie is a sorted tree-based data-structure that stores the set of strings. 
        It has the number of pointers equal to the number of characters of the alphabet in each node.

    3. A heap is a complete binary tree that satisfies the  heap property. 
        There are two types of heaps, the max heap and the min heap:
        The heap property says that is the value of Parent is either greater than or equal to (in a max heap ),
        or less than or equal to (in a min heap) the value of the Child.
"""
