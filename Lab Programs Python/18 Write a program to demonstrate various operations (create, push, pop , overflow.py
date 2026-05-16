# Write a program to demonstrate various operations (create, push, pop , overflow, 
# underflow, peek , display) of STACK using linked list. 

# Program to demonstrate STACK operations using Linked List

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class using Linked List
class Stack:
    def __init__(self, max_size):
        self.top = None
        self.max_size = max_size
        self.size = 0

    # Push operation
    def push(self, data):

        # Overflow condition
        if self.size >= self.max_size:
            print("STACK OVERFLOW")
            return

        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        self.size += 1

        print(data, "pushed into stack")

    # Pop operation
    def pop(self):

        # Underflow condition
        if self.top is None:
            print("STACK UNDERFLOW")
            return

        popped = self.top.data
        self.top = self.top.next

        self.size -= 1

        print(popped, "popped from stack")

    # Peek operation
    def peek(self):

        if self.top is None:
            print("Stack is empty")
            return

        print("Top element is:", self.top.data)

    # Display operation
    def display(self):

        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top

        print("Stack elements are:")

        while temp:
            print(temp.data)
            temp = temp.next


# Main Program
stack = Stack(3)   # Maximum size of stack = 3

# Push operation
stack.push(10)
stack.push(20)
stack.push(30)

# Overflow condition
stack.push(40)

# Display stack
stack.display()

# Peek operation
stack.peek()

# Pop operation
stack.pop()

# Display after pop
stack.display()

# Pop remaining elements
stack.pop()
stack.pop()

# Underflow condition
stack.pop()