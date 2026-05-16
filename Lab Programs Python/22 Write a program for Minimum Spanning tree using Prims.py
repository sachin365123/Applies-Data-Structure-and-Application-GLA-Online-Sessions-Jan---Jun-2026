# 22 Write a program for Minimum Spanning Tree.

# Program to find Minimum Spanning Tree using Prim's Algorithm

INF = 9999999

# Number of vertices
V = 5

# Graph represented using adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [False] * V

# Start from vertex 0
selected[0] = True

edge_count = 0

print("Edges in the Minimum Spanning Tree:")
print("Vertex1 - Vertex2 : Weight")

# MST will have V-1 edges
while edge_count < V - 1:

    minimum = INF
    x = 0
    y = 0

    for i in range(V):
        if selected[i]:

            for j in range(V):

                # Select minimum weight edge
                if (not selected[j]) and graph[i][j]:

                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} : {graph[x][y]}")

    selected[y] = True
    edge_count += 1