# stack ADT

# Fixed Array implementation
# struct stack{
#     int arr[];
#     int top;
#     int maxsize;
# }

class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.arr = [None for i in range(maxsize)]
        # keep track of the number of elements
        self.top = 0

    def peek(self):
        return self.arr[self.top - 1]

    def is_empty(self):
        return self.top == 0

    def push(self, x):
        # if the stack is full
        if self.top == self.maxsize:
            # handle overflow error
            print("The stack is full")
        # if the stack is not full
        else:
            # add the element
            self.arr[self.top] = x
            self.top += 1

    def pop(self):
        # if the stack is empty
        if self.is_empty():
            # handle underflow error
            print("The stack is empty")
        # if the stack is not empty
        else:
            # Last in First Out
            # return the popped value
            x = self.arr[self.top - 1]
            self.top -= 1
            return x

    def display(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            print("The elements in the stack are: ", end=" ")
            for i in range(self.top):
                print(self.arr[i], end=" ")
            print()
