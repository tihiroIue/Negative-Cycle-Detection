import graph
import algorithms

num_iterations = 100

# Graphs with a randomly generated hamiltonian cycle in each graph (large cycles)
graph500_hamiltonian = graph.graph_with_negative_hamiltonian_cycle(500, 3100)
graph1000_hamiltonian = graph.graph_with_negative_hamiltonian_cycle(1000, 6900)
graph2000_hamiltonian = graph.graph_with_negative_hamiltonian_cycle(2000, 15000)
# graph5000_hamiltonian = graph.graph_with_negative_hamiltonian_cycle(5000, 42000)
# graph10000_hamiltonian = graph.graph_with_negative_hamiltonian_cycle(10000, 92000)

# Experiment 1: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least hamiltonian cycle.
# The number of edges is about N*ln(N). N is the number of vertices.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations
count1, count2, count3, count4, count5 = 0, 0, 0, 0, 0
for i in range(num_iterations):
    print(i)
    if(algorithms.negative_cycle_detection(graph500_hamiltonian, 0, 1)[3] == 1): 
        count1 += 1
    if(algorithms.negative_cycle_detection(graph1000_hamiltonian, 0, 1.2)[3] == 1):
        count2 += 1
    if(algorithms.negative_cycle_detection(graph2000_hamiltonian, 0, 1.5)[3] == 1):
        count3 += 1
    #if(algorithms.negative_cycle_detection(graph5000_hamiltonian, 0, 1.5)[3] == 1):
    #    count4 += 1
    # if(algorithms.negative_cycle_detection(graph10000_hamiltonian, 0, 1.5)[3] == 1):
    #    count5 += 1
print("When running the algorithm on graphs with at least one hamiltonian cycle in each cycle and sparse,")
print("The numbers of tests that use more that n/3 + o(n) iterations to detect negative cycles are:")
print(count1, count2, count3, count4, count5, "\n")



# Graphs with a randomly generated cycle of length 3 (small cycles)
graph500_small_cycle = graph.graph_with_negative_cycle(500, 3100, 0, 3)
graph1000_small_cycle = graph.graph_with_negative_cycle(1000, 6900, 0, 3)
graph2000_small_cycle = graph.graph_with_negative_cycle(2000, 15000, 0, 3)
# graph5000_small_cycle = graph.graph_with_negative_cycle(5000, 42000, 0, 3)
# graph10000_small_cycle = graph.graph_with_negative_cycle(10000, 92000, 0, 3)

# Experiment 2: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least a cycle of length 3.
# The number of edges is about N*ln(N). N is the number of vertices.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations.
count1, count2, count3, count4, count5 = 0, 0, 0, 0, 0
for i in range(num_iterations):
    print(i)
    if(algorithms.negative_cycle_detection(graph500_small_cycle, 0, 1)[3] == 1):
        count1 += 1
    if(algorithms.negative_cycle_detection(graph1000_small_cycle, 0, 1.2)[3] == 1):
        count2 += 1
    if(algorithms.negative_cycle_detection(graph2000_small_cycle, 0, 1.5)[3] == 1):
        count3 += 1
    #if(algorithms.negative_cycle_detection(graph5000_small_cycle, 0, 1.5)[3] == 1):
    #    count4 += 1
    # if(algorithms.negative_cycle_detection(graph10000_small_cycle, 0, 1.5)[3] == 1):
    #    count5 += 1
print("When running the algorithm on graphs with at least one cycle of length 3 in each cycle and sparse,")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(count1, count2, count3, count4, count5, "\n")


# Graphs with a randomly generated hamiltonian cycle in each graph (large cycles)
graph500_hamiltonian_dense = graph.graph_with_negative_hamiltonian_cycle(500, 11200)
graph1000_hamiltonian_dense = graph.graph_with_negative_hamiltonian_cycle(1000, 31600)
graph2000_hamiltonian_dense = graph.graph_with_negative_hamiltonian_cycle(2000, 89000)
# graph5000_hamiltonian_dense = graph.graph_with_negative_hamiltonian_cycle(5000, 354000)
# graph10000_hamiltonian_dense = graph.graph_with_negative_hamiltonian_cycle(10000, 1000000)

# Experiment 3: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least hamiltonian cycle.
# The number of edges is about N*square root(N). N is the number of vertices.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations
count1, count2, count3, count4, count5 = 0, 0, 0, 0, 0
for i in range(num_iterations):
    print(i)
    if(algorithms.negative_cycle_detection(graph500_hamiltonian_dense, 0, 1)[3] == 1):
        count1 += 1
    if(algorithms.negative_cycle_detection(graph1000_hamiltonian_dense, 0, 1.2)[3] == 1):
        count2 += 1
    if(algorithms.negative_cycle_detection(graph2000_hamiltonian_dense, 0, 1.5)[3] == 1):
        count3 += 1
    #if(algorithms.negative_cycle_detection(graph5000_hamiltonian_dense, 0, 1.5)[3] == 1):
    #    count4 += 1
    #if(algorithms.negative_cycle_detection(graph10000_hamiltonian_dense, 0, 1.5)[3] == 1):
    #    count5 += 1
print("When running the algorithm on graphs with at least one hamiltonian cycle in each cycle and relatively dense,")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(count1, count2, count3, count4, count5, "\n")



# Graphs with a randomly generated cycle of length 3 (small cycles)
graph500_small_cycle_dense = graph.graph_with_negative_cycle(500, 11200, 0, 3)
graph1000_small_cycle_dense = graph.graph_with_negative_cycle(1000, 31600, 0, 3)
graph2000_small_cycle_dense = graph.graph_with_negative_cycle(2000, 89000, 0, 3)
# graph5000_small_cycle_dense = graph.graph_with_negative_cycle(5000, 354000, 0, 3)
# graph10000_small_cycle_dense = graph.graph_with_negative_cycle(10000, 1000000, 0, 3)

# Experiment 4: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least a cycle of length 3.
# The number of edges is about N*square root(N). N is the number of vertices.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations.
count1, count2, count3, count4, count5 = 0, 0, 0, 0, 0
for i in range(num_iterations):
    print(i)
    if(algorithms.negative_cycle_detection(graph500_small_cycle_dense, 0, 1)[3] == 1):
        count1 += 1
    if(algorithms.negative_cycle_detection(graph1000_small_cycle_dense, 0, 1.2)[3] == 1):
        count2 += 1
    if(algorithms.negative_cycle_detection(graph2000_small_cycle_dense, 0, 1.5)[3] == 1):
        count3 += 1
    #if(algorithms.negative_cycle_detection(graph5000_small_cycle_dense, 0, 1.5)[3] == 1):
    #    count4 += 1
    #if(algorithms.negative_cycle_detection(graph10000_small_cycle_dense, 0, 1.5)[3] == 1):
    #    count5 += 1
print("When running the algorithm on graphs with at least one cycle of length 3 in each cycle and relatively dense,")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(count1, count2, count3, count4, count5, "\n")


# Graphs with a randomly generated hamiltonian cycle in each graph (large cycles)
graph500_hamiltonian_full = graph.graph_with_negative_hamiltonian_cycle(500, 249500)
graph1000_hamiltonian_full = graph.graph_with_negative_hamiltonian_cycle(1000, 999000)
graph2000_hamiltonian_full = graph.graph_with_negative_hamiltonian_cycle(2000, 3998000)
#graph5000_hamiltonian_full = graph.graph_with_negative_hamiltonian_cycle(5000, 24995000)

# Experiment 5: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least hamiltonian cycle.
# The number of edges is about N*square root(N). N is the number of vertices.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations
count1, count2, count3, count4 = 0, 0, 0, 0
for i in range(num_iterations):
    print(i)
    if(algorithms.negative_cycle_detection(graph500_hamiltonian_full, 0, 1)[3] == 1):
        count1 += 1
    if(algorithms.negative_cycle_detection(graph1000_hamiltonian_full, 0, 1.2)[3] == 1):
        count2 += 1
    if(algorithms.negative_cycle_detection(graph2000_hamiltonian_full, 0, 1.5)[3] == 1):
        count3 += 1
    #if(algorithms.negative_cycle_detection(graph5000_hamiltonian_full, 0, 1.5)[3] == 1):
    #    count4 += 1
print("When running the algorithm on graphs with at least one hamiltonian cycle in each cycle and relatively dense,")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(count1, count2, count3, count4, "\n")

# Graphs with a randomly generated cycle of length 3 (small cycles)
graph500_small_cycle_full = graph.graph_with_negative_cycle(500, 249500, 0, 3)
graph1000_small_cycle_full = graph.graph_with_negative_cycle(1000, 999000, 0, 3)
graph2000_small_cycle_full = graph.graph_with_negative_cycle(2000, 3998000, 0, 3)
#graph5000_small_cycle_full = graph.graph_with_negative_cycle(5000, 24995000, 0, 3)

# Experiment 6: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least a cycle of length 3.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations.
count1, count2, count3, count4 = 0, 0, 0, 0
for i in range(num_iterations):
    print(i)
    if(algorithms.negative_cycle_detection(graph500_small_cycle_full, 0, 1)[3] == 1):
        count1 += 1
    if(algorithms.negative_cycle_detection(graph1000_small_cycle_full, 0, 1.2)[3] == 1):
        count2 += 1
    if(algorithms.negative_cycle_detection(graph2000_small_cycle_full, 0, 1.5)[3] == 1):
        count3 += 1
    #if(algorithms.negative_cycle_detection(graph5000_small_cycle_full, 0, 1.5)[3] == 1):
    #    count4 += 1
print("When running the algorithm on graphs with at least one cycle of length 3 in each cycle and very dense,")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(count1, count2, count3, count4, "\n")