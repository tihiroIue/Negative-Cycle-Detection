import graph
import random
import math

# Auxiliary function for initialization of predecessors and distances.
# It returns a dictionary of all vertices, and the values are the distances to the source (set to be infinity at first) and
# predecessors (set to the None at first).
def initialization(graph, source):
    dist, pred = {}, {}
    for v in graph:
        dist[v], pred[v] = float('inf'), None
    dist[source] = 0
    return (dist, pred)

# The bellman-ford algorithm for computing the shortest path from a single sourse.
def bellman_Ford(graph, source):
    dist, pred = initialization(graph, source)
    num_vertices = len(graph)
    count_iteration, count_relaxation = 0, 0
    for _ in range(num_vertices - 1):
        count_iteration += 1
        # Relax all edges from vertices whose distances were changed in the latest iteration
        for u in range(num_vertices):
            for v, w in graph[u].items():
                count_relaxation += 1
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
    for u in range(num_vertices):
        for v, w in graph[u].items():
            if dist[v] > dist[v] + w:
                return (False, dist, pred, count_iteration, count_relaxation)
    return (True, dist, pred, count_iteration, count_relaxation)

# The bellman-ford algorithm for computing the shortest path from a single sourse.
def adaptive_bellman_Ford(graph, source):
    dist, pred = initialization(graph, source)
    num_vertices = len(graph)
    changed = set([source])
    newly_changed = set()
    count_iteration, count_relaxation = 0, 0
    while changed != set() and count_iteration < num_vertices - 1:
        newly_changed = set()
        count_iteration += 1
        # Relax all edges from vertices whose distances were changed in the latest iteration
        for u in changed:
            for v, w in graph[u].items():
                count_relaxation += 1
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    newly_changed.add(v)
        changed = newly_changed.copy()
    for u in range(num_vertices):
        for v, w in graph[u].items():
            if dist[v] > dist[u] + w:
                return (False, dist, pred, count_iteration, count_relaxation)
    return (True, dist, pred, count_iteration, count_relaxation)

# The randomized Yen's algorithm with adaptive improvement of Bellman-ford.
def randomized(graph, source):
    # Divide the original graph into 2 subgraphs, one consists of edges from vertices with higher number and vice versa
    vertices_num = [*range(len(graph))]
    vertices_order = vertices_num.copy()
    for i in range(len(graph)):
        vertices_order[i] = random.random()
    # Set the number of the source to be -1, so that the source always gets the smallest number.
    vertices_order[source] = -1
    num_vertices = len(graph)
    graph_plus, graph_minus = {}, {}
    for v in range(num_vertices):
        graph_plus[v], graph_minus[v] = {}, {}
    for u in range(num_vertices):
        for v, w in graph[u].items():
            if vertices_order[v] > vertices_order[u]:
                graph_plus[u][v] = w
            else:
                graph_minus[u][v] = w

    vertices_and_order = list(zip(vertices_num, vertices_order))
    def order(v):
        return v[1]
    increasing_vertices = sorted(vertices_and_order, key=order)
    decreasing_vertices = sorted(vertices_and_order, key=order, reverse=True)

    dist, pred = initialization(graph, source)
    changed = set()
    newly_changed = set()
    changed.add(source)
    count_iteration, count_relaxation = 0, 0
    while changed != set() and count_iteration < (num_vertices // 2 + 1):
        count_iteration += 1
        for u, _ in increasing_vertices:
            if u in changed or u in newly_changed:
                for v, w in graph_plus[u].items():
                    count_relaxation += 1
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        newly_changed.add(v)
        for u, _ in decreasing_vertices:
            if u in changed or u in newly_changed:
                for v, w in graph_minus[u].items():
                    count_relaxation += 1
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        newly_changed.add(v)
        changed, newly_changed = newly_changed.copy(), set()
        
    for u in range(num_vertices):
        for v, w in graph[u].items():
            if dist[v] > dist[u] + w:
                return (False, dist, pred, count_iteration, count_relaxation)
            
    return (True, dist, pred, count_iteration, count_relaxation)


# Auxiliary function for detecting a cycle in the parent graph
# (a graph that reverses the directions of all edges in the predecessor subgraph).
# It returns True if a cycle (regardless the sum) and a False otherwise.
# We do this by running a depth-first search to detect a back edge in the original graph (if any).
# The code is referred to: https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
def subgraph_traversal(pred_graph):
    visited, stack = [False] * len(pred_graph), [False] * len(pred_graph)
    for u in pred_graph.keys():
        if not visited[u] and traversal_helper(pred_graph, u, visited, stack):
            return True
    return False
    
# A helper function for running the DFS recursively.
def traversal_helper(pred_graph, vertex, visted, stack):
    visted[vertex], stack[vertex] = True, True
    v = pred_graph[vertex]
    if v != None and not visted[v] and traversal_helper(pred_graph, v, visted, stack):
        return True
    elif v != None and stack[v]:
        return True
    stack[vertex] = False
    return False

# An algorithm for negative weight cycle detection with randomized bellman-ford.
def negative_cycle_detection(graph, source, c):
    # Divide the original graph into 2 subgraphs, one consists of edges from vertices with higher number and vice versa
    vertices_num = [*range(len(graph))]
    vertices_order = vertices_num.copy()
    for i in range(len(graph)):
        vertices_order[i] = random.random()
    # Set the number of the source to be -1, so that the source always gets the smallest number.
    vertices_order[source] = -1
    num_vertices = len(graph)
    graph_plus, graph_minus = {}, {}
    for v in range(num_vertices):
        graph_plus[v], graph_minus[v] = {}, {}
    for u in range(num_vertices):
        for v, w in graph[u].items():
            if vertices_order[v] > vertices_order[u]:
                graph_plus[u][v] = w
            else:
                graph_minus[u][v] = w

    vertices_and_order = list(zip(vertices_num, vertices_order))
    def order(v):
        return v[1]
    increasing_vertices = sorted(vertices_and_order, key=order)
    decreasing_vertices = sorted(vertices_and_order, key=order, reverse=True)

    dist, pred = initialization(graph, source)
    changed = set()
    changed.add(source)
    newly_changed1, newly_changed2 = set(), set()
    count_iteration, count_relaxation = 0, 0
    count_traversal = 0
    while changed != set() and count_iteration < (num_vertices // 2 + 1):
        count_iteration += 1
        for u, _ in increasing_vertices:
            if u in changed or u in newly_changed1:
                for v, w in graph_plus[u].items():
                    count_relaxation += 1
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        newly_changed1.add(v)
        for u, _ in decreasing_vertices:
            if u in changed or u in newly_changed2:
                for v, w in graph_minus[u].items():
                    count_relaxation += 1
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        newly_changed2.add(v)
        changed, newly_changed1, newly_changed2 = newly_changed1.union(newly_changed2), set(), set()

        if count_iteration >= (num_vertices / 3 + 2 + math.sqrt(2 * c * num_vertices * math.log10(num_vertices))):
            count_traversal += 1
            if subgraph_traversal(pred):
                return (False, dist, pred, count_traversal, count_iteration, count_relaxation)
            
    for u in range(num_vertices):
        for v, w in graph[u].items():
            if dist[v] > dist[u] + w:
                return (False, dist, pred, count_traversal,  count_iteration, count_relaxation)

    return (True, dist, pred, count_traversal, count_iteration, count_relaxation)

# An algorithm for negative weight cycle detection with randomized bellman-ford.
def negative_cycle_detection_modified(graph, source):
    # Divide the original graph into 2 subgraphs, one consists of edges from vertices with higher number and vice versa
    vertices_num = [*range(len(graph))]
    vertices_order = vertices_num.copy()
    random.shuffle(vertices_order)
    num_vertices = len(graph)
    graph_plus, graph_minus = {}, {}
    for v in range(num_vertices):
        graph_plus[v], graph_minus[v] = {}, {}
    for u in range(num_vertices):
        for v, w in graph[u].items():
            if vertices_order[v] > vertices_order[u]:
                graph_plus[u][v] = w
            else:
                graph_minus[u][v] = w

    vertices_and_order = list(zip(vertices_num, vertices_order))
    def order(v):
        return v[1]
    increasing_vertices = sorted(vertices_and_order, key=order)
    decreasing_vertices = sorted(vertices_and_order, key=order, reverse=True)

    dist, pred = initialization(graph, source)
    changed = set()
    changed.add(source)
    newly_changed1, newly_changed2 = set(), set()
    count_iteration, count_relaxation = 0, 0
    while changed != set() and count_iteration < (num_vertices // 2 + 1):
        count_iteration += 1
        for u, _ in increasing_vertices:
            if u in changed or u in newly_changed1:
                for v, w in graph_plus[u].items():
                    count_relaxation += 1
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        newly_changed1.add(v)
        for u, _ in decreasing_vertices:
            if u in changed or u in newly_changed2:
                for v, w in graph[u].items():
                    count_relaxation += 1
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        newly_changed2.add(v)
        changed, newly_changed1, newly_changed2 = newly_changed1.union(newly_changed2), set(), set()

        if subgraph_traversal(pred):
            return (False, dist, pred, count_iteration, count_relaxation)
            
    for u in range(num_vertices):
        for v, w in graph[u].items():
            if dist[v] > dist[u] + w:
                return (False, dist, pred)
    return (True, dist, pred, count_iteration, count_relaxation)

# Some simple testings.
if __name__ == "__main__":
    example_graph1 = {
    0: {1: -1},
    1: {2: 1},
    2: {3: 1, 5: 3},
    3: {4: 2},
    4: {5: 2},
    5: {}
    }

    example_graph2 = {
        0: {1: -1},
        1: {2: 1},
        2: {3: 1, 5: 3},
        3: {4: -2},
        4: {5: 2},
        5: {1: -5}
    }

    example_graph3 = graph.graph_generator(100, 900, False)
    example_graph4 = graph.graph_generator(100, 900, True)

    example_graph5 = graph.graph_generator(1000, 900000, False)
    example_graph6 = graph.graph_generator(10000, 90000, True)

    example_graph7 = graph.graph_generator(2000, 3000000, True)
    example_graph8 = graph.graph_generator(2000, 3900000, False)
    example_graph8 = graph.graph_generator(2000, 3990000, False)

    example_graph9 = graph.graph_generator(500, 249500, False)

    example_subgraph1 = {0: None, 1: 2, 2: 0, 3: None, 4: 3, 5: 4, 6: 7, 7: 6}
    example_subgraph2 = {0: 1, 1: 2, 2: 3, 3: 0, 4: 3, 5: 4, 6: 7, 7: 6}
    example_subgraph3 = {0: 1, 1: 2, 2: 3, 3: 4, 4: None, 5: 6, 6: 7, 7: 8, 8: 5}

    # negative_cycle_detection(example_graph7, 0, 2)

    # assert(subgraph_traversal(example_graph7) == True)
    # assert(subgraph_traversal(example_graph8) == True)
    # assert(subgraph_traversal(example_graph9) == True)

    # assert(randomized(example_graph3, 0)[1] == adaptive_bellman_Ford(example_graph3, 0)[1])
    # assert(randomized(example_graph4, 0)[0] == adaptive_bellman_Ford(example_graph4, 0)[0])
    # assert(randomized(example_graph5, 0)[1] == bellman_Ford(example_graph5, 0)[1])
    
    # print(adaptive_bellman_Ford(example_graph9, 0)[0])
    sum1, sum2 = 0, 0

    for i in range(1000):
        sum1 += adaptive_bellman_Ford(example_graph9, 0)[4]
        sum2 += randomized(example_graph9, 0)[4]
    print(sum1/1000, sum2/1000)
    
    """
    for i in range(100):
        example_graph = graph.graph_generator(1000, 9000, True)
        assert(negative_cycle_detection(example_graph, 0, 2)[0] == randomized(example_graph, 0)[0])
        # example_graph = graph.graph_generator(100, 900, False)
        # assert(negative_cycle_detection(example_graph, 0, 2)[1] == randomized(example_graph, 0)[1])
    """
