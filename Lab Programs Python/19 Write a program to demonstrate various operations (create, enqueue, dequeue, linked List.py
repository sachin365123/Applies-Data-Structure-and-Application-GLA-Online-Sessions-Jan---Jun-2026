# 19 Write a program to demonstrate various operations (create, enqueue, dequeue, 
# overflow, underflow, peek, display) of QUEUE using linked list. 


# Program to demonstrate QUEUE operations using Linked List

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue class using Linked List
class Queue:
    def __init__(self, max_size):
        self.front = None
        self.rear = None
        self.size = 0
        self.max_size = max_size

    # Enqueue operation
    def enqueue(self, data):

        # Overflow condition
        if self.size >= self.max_size:
            print("QUEUE OVERFLOW")
            return

        new_node = Node(data)

        # If queue is empty
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

        print(data, "inserted into queue")

    # Dequeue operation
    def dequeue(self):

        # Underflow condition
        if self.front is None:
            print("QUEUE UNDERFLOW")
            return

        removed = self.front.data
        self.front = self.front.next

        # If queue becomes empty
        if self.front is None:
            self.rear = None

        self.size -= 1

        print(removed, "deleted from queue")

    # Peek operation
    def peek(self):

        if self.front is None:
            print("Queue is empty")
            return

        print("Front element is:", self.front.data)

    # Display operation
    def display(self):

        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front

        print("Queue elements are:")

        while temp:
            print(temp.data, end=" <- ")
            temp = temp.next

        print("NULL")


# Main Program
queue = Queue(3)   # Maximum size of queue = 3

# Enqueue operation
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Overflow condition
queue.enqueue(40)

# Display queue
queue.display()

# Peek operation
queue.peek()

# Dequeue operation
queue.dequeue()

# Display after dequeue
queue.display()

# Remove remaining elements
queue.dequeue()
queue.dequeue()

# Underflow condition
queue.dequeue()