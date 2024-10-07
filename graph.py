import random
from collections import deque

# Auxiliary function for generating random graphs with a certain number of vertices and edges.
def graph_generator(size_V, size_E, negative):
    graph = {}
    num_edges = 0
    for i in range(size_V):
        graph[i] = {}
    prob = size_E / (size_V * size_V)
    while num_edges < size_E:
        for i in range(size_V):
            for j in range(size_V):
                if i != j:
                    if size_E == size_V * (size_V - 1):
                        num_edges += 1
                        if negative:
                            graph[i][j] = random.randint(-100, 100)
                        else:
                            graph[i][j] = random.randint(1, 100)
                    else:
                        if random.random() < prob and j not in graph[i].keys():
                            if negative:
                                graph[i][j] = random.randint(-100, 100)
                            else:
                                graph[i][j] = random.randint(1, 100)
                            num_edges += 1
                    if num_edges == size_E:
                        break
            if num_edges == size_E:
                break
    return graph

# Auxiliary function for generating graphs with a negative cycle of a given length.
def graph_with_negative_cycle(num_V, num_E, source, length):
    graph = graph_generator(num_V, num_E, False)
    # First find all reachable vertices from the source via breath first search.
    # Reference: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    reachable_vertice = []
    reachable_vertice += [source]
    q = deque()
    q.append(source)
    while q != deque():
        u = q.popleft()
        for v in graph[u].keys():
            if v not in reachable_vertice:
                reachable_vertice += [v]
                q.append(v)
    # Select a give number of vertices and generate a negative cycle.
    random.shuffle(reachable_vertice)
    sum = 0
    for i in range(length):
        if i + 1 == length:
            u, v = reachable_vertice[i], reachable_vertice[0]
            graph[u][v] = - sum - 1
        else:
            u, v = reachable_vertice[i], reachable_vertice[i + 1]
            graph[u][v] = graph[u][v] = random.randint(-100, 100)
            sum += graph[u][v]
    return graph

# Auxiliary function for generating graphs with a negative hamiltonian cycle.
def graph_with_negative_hamiltonian_cycle(num_V, num_E):
    graph = graph_generator(num_V, num_E, False)
    # Generate the order of vertices in the hamiltonian cycle randomly.
    vertices = list(range(num_V))
    random.shuffle(vertices)
    sum = 0
    for i in range(num_V):
        if i + 1 == num_V:
            u, v = vertices[i], vertices[0]
            graph[u][v] = - sum - 1
        else:
            u, v = vertices[i], vertices[i + 1]
            graph[u][v] = random.randint(-100, 100)
            sum += graph[u][v]
    return graph

if __name__ == "__main__":
    graph1 = graph_generator(10, 10, True)
    graph2 = graph_generator(10, 30, False)
    graph3 = graph_generator(1000, 30000, False)
    graph4 = graph_with_negative_hamiltonian_cycle(3, 3)
    print(graph4)