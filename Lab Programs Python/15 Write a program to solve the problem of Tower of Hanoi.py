# Write a program to solve the problem of Tower of Hanoi 
# by using recursion. 

# Python Program to Solve Tower of Hanoi using Recursion

def tower_of_hanoi(n, source, auxiliary, destination):
    
    # Base Case
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")


    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Main Program
n = int(input("Enter the number of disks: "))

tower_of_hanoi(n, 'A', 'B', 'C')