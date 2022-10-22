"""
Linked Lists
    - Node that point to the next node.
    - Head is first node.
    - Tail is last node.
    - Last node points to None.
    - Nodes can be thought of as dictionaries:
        {
            "value": 4,
            "next": None 
        }


Difference between Lists and Linked Lists:
    - List are made up contiguous indexed places in memory.
    - Linked Lists are made up of nodes that are not indexed rather placed throughout memory
        in a scattered manner. Data is not lost as nodes point to the next node in memory.
"""



"""
Append Method:
- Appending a a new node to end of linked list.

"""



"""
Linked List in class and constructor set-up. 
"""
# creates a new node and only creates new nodes.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self, value):
        new_node = Node(value) # calls the Node class to create a new node.
        self.head = new_node # assigning the new node to head pointer.
        self.tail = new_node # assigning the new node to the tail pointer.
        self.length = 1 # assigning linked list length to 1. 

    def print_list(self):
        temp = self.head
        print(my_linked_list.head.value)
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value) # creating a node.

        # testing to see if list is empty.
        if self.head is None:
        # if self.length == 0:
            self.head = new_node # if list is empty assign head and tail pointers to new node.
            self.tail = new_node
        else:
            self.tail.next = new_node # if list not not empty assign tail pointer to new node.
            self.tail = new_node
        self.length += 1 # increase the length of linked list by 1.
        return True

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.print_list()

