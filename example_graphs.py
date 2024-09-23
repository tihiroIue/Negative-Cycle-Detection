import graph
import algorithms

# We test graphs with 500, 1000, 2000, 5000 and 10000 vertices.
# The number of edges is about  N * ln N, where N is the number of vertices.

graph500 = graph.graph_generator(500, 3100, True)
while algorithms.bellman_Ford(graph500, 0)[0] == True:
    graph500 = graph.graph_generator(500, 1500, True)

graph1000 = graph.graph_generator(1000, 6900, True)
while algorithms.bellman_Ford(graph1000, 0)[0] == True:
    graph1000 = graph.graph_generator(1000, 3000, True)

graph2000 = graph.graph_generator(2000, 15000, True)
while algorithms.bellman_Ford(graph2000, 0)[0] == True:
    graph2000 = graph.graph_generator(2000, 6600, True)

graph5000 = graph.graph_generator(5000, 42000, True)
while algorithms.bellman_Ford(graph5000, 0)[0] == True:
    graph5000 = graph.graph_generator(5000, 18000, True)

graph10000 = graph.graph_generator(10000, 92000, True)
while algorithms.bellman_Ford(graph10000, 0)[0] == True:
    graph10000 = graph.graph_generator(10000, 40000, True)

