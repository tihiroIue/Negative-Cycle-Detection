import random

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
def graph_with_negative_cycle(num_V, num_E, length):
    pass

# Auxiliary function for generating graphs with a negative hamiltonian cycle.
def graph_with_negative_hamiltonian_cycle(num_V, num_E, length):
    graph = graph_generator(num_V, num_E, False)
    vertices = list(range(num_V))
    vertices_order = random.shuffle(vertices)
    pass

if __name__ == "__main__":
    graph1 = graph_generator(10, 10, True)
    graph2 = graph_generator(10, 30, False)
    graph3 = graph_generator(1000, 30000, False)
    print(graph1)