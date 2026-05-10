# 12 Write a program to demonstrate various operations (create, push, pop , overflow, 
# underflow, peek , display) of STACK using array implementation. 

# Python program to demonstrate STACK operations using array implementation

MAX = 5
stack = []
top = -1

# PUSH operation
def push():
    global top

    if top == MAX - 1:
        print("Stack Overflow")
    else:
        element = int(input("Enter element to push: "))
        stack.append(element)
        top += 1
        print(element, "pushed into stack")

# POP operation
def pop():
    global top

    if top == -1:
        print("Stack Underflow")
    else:
        removed = stack[top]
        del stack[top]
        top -= 1
        print(removed, "popped from stack")

# PEEK operation
def peek():
    if top == -1:
        print("Stack is empty")
    else:
        print("Top element is:", stack[top])

# DISPLAY operation
def display():
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack elements are:")
        for i in range(top, -1, -1):
            print(stack[i])


# Main Menu
while True:
    print("\n----- STACK OPERATIONS -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

