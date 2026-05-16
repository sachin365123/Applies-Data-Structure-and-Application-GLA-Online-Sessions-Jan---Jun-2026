# 21 Write a program to illustrate traversal of a graph using Breadth- first search. 

# Program to illustrate Breadth First Search (BFS) Traversal of a Graph

from collections import deque

# BFS function
def bfs(graph, start):

    visited = set()          # To keep track of visited nodes
    queue = deque()          # Queue for BFS

    visited.add(start)
    queue.append(start)

    print("BFS Traversal:")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        # Visit all adjacent vertices
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Graph represented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting node
start_node = 'A'

# Call BFS
bfs(graph, start_node)