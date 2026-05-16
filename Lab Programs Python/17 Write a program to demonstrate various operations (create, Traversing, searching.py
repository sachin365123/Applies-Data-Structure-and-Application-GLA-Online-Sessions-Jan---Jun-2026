# Write a program to demonstrate various operations (create, Traversing, searching, 
# inserting an element at beginning, at end, after a given element, deleting an element 
# from beginning, from end, after a given element) of a doubly linked list. 

# Program to demonstrate various operations of Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Create / Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insert after a given element
    def insert_after(self, key, data):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Element not found")
            return

        new_node = Node(data)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # Traverse / Display
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        print("Doubly Linked List:")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # Search an element
    def search(self, key):
        temp = self.head
        pos = 1

        while temp:
            if temp.data == key:
                print(f"Element {key} found at position {pos}")
                return

            temp = temp.next
            pos += 1

        print("Element not found")

    # Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

        print("Node deleted from beginning")

    # Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Only one node
        if temp.next is None:
            self.head = None
            print("Node deleted from end")
            return

        while temp.next:
            temp = temp.next

        temp.prev.next = None

        print("Node deleted from end")

    # Delete after a given element
    def delete_after(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Given element not found")
            return

        if temp.next is None:
            print("No node exists after given element")
            return

        node_to_delete = temp.next

        temp.next = node_to_delete.next

        if node_to_delete.next:
            node_to_delete.next.prev = temp

        print(f"Node after {key} deleted")


# Main Program
dll = DoublyLinkedList()

# Creating list
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)

dll.traverse()

# Insert at beginning
dll.insert_beginning(5)
dll.traverse()

# Insert at end
dll.insert_end(40)
dll.traverse()

# Insert after given element
dll.insert_after(20, 25)
dll.traverse()

# Search element
dll.search(30)

# Delete from beginning
dll.delete_beginning()
dll.traverse()

# Delete from end
dll.delete_end()
dll.traverse()

# Delete after a given element
dll.delete_after(20)
dll.traverse()