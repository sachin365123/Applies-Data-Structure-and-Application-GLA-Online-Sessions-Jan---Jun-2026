# Write a program to demonstrate various operations (create, enqueue, dequeue, 
# overflow, underflow, peek, display) of CIRCULAR QUEUE using array 
# implementation. 

# Python Program to Demonstrate Circular Queue Operations
# Operations: Create, Enqueue, Dequeue, Overflow, Underflow, Peek, Display

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue Operation
    def enqueue(self, data):
        # Overflow Condition
        if ((self.rear + 1) % self.size == self.front):
            print("Queue Overflow")
            return

        # First Element Insertion
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data
        print(f"{data} inserted into queue")   

    # Dequeue Operation
    def dequeue(self):
        # Underflow Condition
        if self.front == -1:
            print("Queue Underflow")
            return

        removed_element = self.queue[self.front]

        # Queue has only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"{removed_element} deleted from queue")

     # Peek Operation
    def peek(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Front element is:", self.queue[self.front])

    # Display Operation
    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        print("Circular Queue Elements are:")

        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")

        print()


# Main Program
size = int(input("Enter size of Circular Queue: "))
cq = CircularQueue(size)  

while True:
    print("\n--- Circular Queue Operations ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element to insert: "))
        cq.enqueue(value)

    elif choice == 2:
        cq.dequeue()

    elif choice == 3:
        cq.peek()

    elif choice == 4:
        cq.display()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")