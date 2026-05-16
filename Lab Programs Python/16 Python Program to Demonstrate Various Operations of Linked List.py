# Write a program to demonstrate various operations (create, Traversing, searching, 
# inserting an element at beginning, at end, after a given element, deleting an element 
# from beginning, from end, after a given element) of a linked list. 

# Python Program to Demonstrate Various Operations of Linked List

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # Create / Insert at End
    def create(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Traversing
    def traverse(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        temp = self.head
        print("Linked List Elements are:")

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")

    # Searching
    def search(self, key):
        temp = self.head
        position = 1

        while temp:
            if temp.data == key:
                print(f"Element {key} found at position {position}")
                return
            temp = temp.next
            position += 1

        print("Element not found")

    # Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"{data} inserted at beginning")

    # Insert at End
    def insert_end(self, data):
        self.create(data)
        print(f"{data} inserted at end")

    # Insert after a given element
    def insert_after(self, key, data):
        temp = self.head

        while temp:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                print(f"{data} inserted after {key}")
                return
            temp = temp.next

        print("Given element not found")

    # Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        removed = self.head.data
        self.head = self.head.next
        print(f"{removed} deleted from beginning")

    # Delete from End
    def delete_end(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        temp = self.head

        if temp.next is None:
            removed = temp.data
            self.head = None
            print(f"{removed} deleted from end")
            return

        while temp.next.next:
            temp = temp.next

        removed = temp.next.data
        temp.next = None
        print(f"{removed} deleted from end")

    # Delete after a given element
    def delete_after(self, key):
        temp = self.head

        while temp and temp.next:
            if temp.data == key:
                removed = temp.next.data
                temp.next = temp.next.next
                print(f"{removed} deleted after {key}")
                return
            temp = temp.next

        print("Deletion not possible")


# Main Program
ll = LinkedList()

while True:
    print("\n--- LINKED LIST OPERATIONS ---")
    print("1. Create")
    print("2. Traverse")
    print("3. Search")
    print("4. Insert at Beginning")
    print("5. Insert at End")
    print("6. Insert after Given Element")
    print("7. Delete from Beginning")
    print("8. Delete from End")
    print("9. Delete after Given Element")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        ll.create(value)

    elif choice == 2:
        ll.traverse()

    elif choice == 3:
        key = int(input("Enter element to search: "))
        ll.search(key)

    elif choice == 4:
        value = int(input("Enter element: "))
        ll.insert_beginning(value)

    elif choice == 5:
        value = int(input("Enter element: "))
        ll.insert_end(value)

    elif choice == 6:
        key = int(input("Insert after which element?: "))
        value = int(input("Enter new element: "))
        ll.insert_after(key, value)

    elif choice == 7:
        ll.delete_beginning()

    elif choice == 8:
        ll.delete_end()

    elif choice == 9:
        key = int(input("Delete element after which element?: "))
        ll.delete_after(key)

    elif choice == 10:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")