# 13 Write a program to demonstrate various operations (create, enqueue, dequeue, 
# overflow, underflow, peek, display) of QUEUE using array implementation. 

# Python program to demonstrate QUEUE operations using array implementation

MAX = 5
queue = []
front = -1
rear = -1

# ENQUEUE operation
def enqueue():
    global front, rear

    if rear == MAX - 1:
        print("Queue Overflow")

    else:
        element = int(input("Enter element to enqueue: "))

        if front == -1:
            front = 0

        rear += 1
        queue.append(element)

        print(element, "inserted into queue")

# DEQUEUE operation
def dequeue():
    global front, rear

    if front == -1 or front > rear:
        print("Queue Underflow")

    else:
        removed = queue[0]

        # Shift elements to left
        for i in range(rear):
            queue[i] = queue[i + 1]

        del queue[rear]
        rear -= 1

        if rear == -1:
            front = -1

        print(removed, "deleted from queue")


# PEEK operation
def peek():
    if front == -1:
        print("Queue is empty")

    else:
        print("Front element is:", queue[0])


# DISPLAY operation
def display():
    if front == -1:
        print("Queue is empty")

    else:
        print("Queue elements are:")

        for i in range(front, rear + 1):
            print(queue[i])


# Main Menu
while True:
    print("\n----- QUEUE OPERATIONS -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")