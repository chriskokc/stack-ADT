# stack ADT

# Linked list Head implementation
# struct stack {
#   node* head;
#   int count
# }
from node import Node


class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, x):
        # linked list can dynamically allocate nodes
        # create a new node
        new_node = Node(x)
        # create a connection to the head of the stack
        new_node.next = self.head
        # reassign the head of the stack to the new node connected
        self.head = new_node
        # increment count by 1 as it keeps track of the number of elements
        self.count += 1

    def pop(self):
        # if the stack is empty
        if self.count == 0:
            print("The stack is empty")
        # if the stack is not empty
        else:
            # Last In First Out
            # store the value of the head of the stack
            x = self.head.value
            # move the head of the stack to the second node
            self.head = self.head.next
            # decrement the count by 1
            self.count -= 1
            # return the stored value
            return x
