import graph
import algorithms

num_iterations = 100

"""
# Graphs with a randomly generated hamiltonian cycle in each graph (large cycles)
graph500_hamiltonian = graph.graph_with_negative_hamiltonian_cycle(500, 3100)
graph1000_hamiltonian = graph.graph_with_negative_hamiltonian_cycle(1000, 6900)
graph2000_hamiltonian = graph.graph_with_negative_hamiltonian_cycle(2000, 15000)
graph5000_hamiltonian = graph.graph_with_negative_hamiltonian_cycle(5000, 42000)
graph10000_hamiltonian = graph.graph_with_negative_hamiltonian_cycle(10000, 92000)

# Experiment 1: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least hamiltonian cycle.
# The number of edges is about N*ln(N). N is the number of vertices.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations
counter_list1, counter_list2, counter_list3, counter_list4, counter_list5 = [], [], [], [], []
for _ in range(num_iterations):
    counter_list1 += [algorithms.negative_cycle_detection_modified(graph500_hamiltonian, 0)[3]]
    counter_list2 += [algorithms.negative_cycle_detection_modified(graph1000_hamiltonian, 0)[3]]
    counter_list3 += [algorithms.negative_cycle_detection_modified(graph2000_hamiltonian, 0)[3]]
    counter_list4 += [algorithms.negative_cycle_detection_modified(graph5000_hamiltonian, 0)[3]]
    counter_list5 += [algorithms.negative_cycle_detection_modified(graph10000_hamiltonian, 0)[3]]
average1, average2 = sum(counter_list1) / num_iterations, sum(counter_list2) / num_iterations
average3, average4 = sum(counter_list3) / num_iterations, sum(counter_list4) / num_iterations
average5 = sum(counter_list5) / num_iterations
count1 = [c for c in counter_list1 if c > 500 / 3]
count2 = [c for c in counter_list2 if c > 1000 / 3]
count3 = [c for c in counter_list3 if c > 2900 / 3]
count4 = [c for c in counter_list4 if c > 5000 / 3]
count5 = [c for c in counter_list5 if c > 10000 / 3]
print("When running the algorithm on graphs with at least one hamiltonian cycle in each cycle and sparse,")
print("The average iterations to detect the negative cycle is: ")
print(average1, " when the graph consist of 500 vertices and 3100 edges,")
print(average2, " when the graph consist of 1000 vertices and 6900 edges,")
print(average3, " when the graph consist of 2000 vertices and 15000 edges,")
print(average4, " when the graph consist of 5000 vertices and 42000 edges,")
print(average5, " when the graph consist of 10000 vertices and 92000 edges.")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(len(count1), len(count2), len(count3), len(count4), len(count5), "\n")



# Graphs with a randomly generated cycle of length 3 (small cycles)
graph500_small_cycle = graph.graph_with_negative_cycle(500, 3100, 0, 3)
graph1000_small_cycle = graph.graph_with_negative_cycle(1000, 6900, 0, 3)
graph2000_small_cycle = graph.graph_with_negative_cycle(2000, 15000, 0, 3)
graph5000_small_cycle = graph.graph_with_negative_cycle(5000, 42000, 0, 3)
graph10000_small_cycle = graph.graph_with_negative_cycle(10000, 92000, 0, 3)

# Experiment 2: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least a cycle of length 3.
# The number of edges is about N*ln(N). N is the number of vertices.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations.
counter_list1, counter_list2, counter_list3, counter_list4, counter_list5 = [], [], [], [], []
for _ in range(num_iterations):
    counter_list1 += [algorithms.negative_cycle_detection_modified(graph500_small_cycle, 0)[3]]
    counter_list2 += [algorithms.negative_cycle_detection_modified(graph1000_small_cycle, 0)[3]]
    counter_list3 += [algorithms.negative_cycle_detection_modified(graph2000_small_cycle, 0)[3]]
    counter_list4 += [algorithms.negative_cycle_detection_modified(graph5000_small_cycle, 0)[3]]
    counter_list5 += [algorithms.negative_cycle_detection_modified(graph10000_small_cycle, 0)[3]]
average1, average2 = sum(counter_list1) / num_iterations, sum(counter_list2) / num_iterations
average3, average4 = sum(counter_list3) / num_iterations, sum(counter_list4) / num_iterations
average5 = sum(counter_list5) / num_iterations
count1 = [c for c in counter_list1 if c > 500 / 3]
count2 = [c for c in counter_list2 if c > 1000 / 3]
count3 = [c for c in counter_list3 if c > 2900 / 3]
count4 = [c for c in counter_list4 if c > 5000 / 3]
count5 = [c for c in counter_list5 if c > 10000 / 3]
print("When running the algorithm on graphs with at least one cycle of length 3 in each cycle and sparse,")
print("The average iterations to detect the negative cycle is: ")
print(average1, " when the graph consist of 500 vertices and 3100 edges,")
print(average2, " when the graph consist of 1000 vertices and 6900 edges,")
print(average3, " when the graph consist of 2000 vertices and 15000 edges,")
print(average4, " when the graph consist of 5000 vertices and 42000 edges,")
print(average5, " when the graph consist of 10000 vertices and 92000 edges.")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(len(count1), len(count2), len(count3), len(count4), len(count5), "\n")


# Graphs with a randomly generated hamiltonian cycle in each graph (large cycles)
graph500_hamiltonian_dense = graph.graph_with_negative_hamiltonian_cycle(500, 11200)
graph1000_hamiltonian_dense = graph.graph_with_negative_hamiltonian_cycle(1000, 31600)
graph2000_hamiltonian_dense = graph.graph_with_negative_hamiltonian_cycle(2000, 89000)
graph5000_hamiltonian_dense = graph.graph_with_negative_hamiltonian_cycle(5000, 354000)
graph10000_hamiltonian_dense = graph.graph_with_negative_hamiltonian_cycle(10000, 1000000)

# Experiment 3: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least hamiltonian cycle.
# The number of edges is about N*square root(N). N is the number of vertices.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations
counter_list1, counter_list2, counter_list3, counter_list4, counter_list5 = [], [], [], [], []
for _ in range(num_iterations):
    counter_list1 += [algorithms.negative_cycle_detection_modified(graph500_hamiltonian_dense, 0)[3]]
    counter_list2 += [algorithms.negative_cycle_detection_modified(graph1000_hamiltonian_dense, 0)[3]]
    counter_list3 += [algorithms.negative_cycle_detection_modified(graph2000_hamiltonian_dense, 0)[3]]
    counter_list4 += [algorithms.negative_cycle_detection_modified(graph5000_hamiltonian_dense, 0)[3]]
    counter_list5 += [algorithms.negative_cycle_detection_modified(graph10000_hamiltonian_dense, 0)[3]]
average1, average2 = sum(counter_list1) / num_iterations, sum(counter_list2) / num_iterations
average3, average4 = sum(counter_list3) / num_iterations, sum(counter_list4) / num_iterations
average5 = sum(counter_list5) / num_iterations
count1 = [c for c in counter_list1 if c > 500 / 3]
count2 = [c for c in counter_list2 if c > 1000 / 3]
count3 = [c for c in counter_list3 if c > 2900 / 3]
count4 = [c for c in counter_list4 if c > 5000 / 3]
count5 = [c for c in counter_list5 if c > 10000 / 3]
print("When running the algorithm on graphs with at least one hamiltonian cycle in each cycle and relatively dense,")
print("The average iterations to detect the negative cycle is: ")
print(average1, " when the graph consist of 500 vertices and 11200 edges,")
print(average2, " when the graph consist of 1000 vertices and 31600 edges,")
print(average3, " when the graph consist of 2000 vertices and 89000 edges,")
print(average4, " when the graph consist of 5000 vertices and 354000 edges,")
print(average5, " when the graph consist of 10000 vertices and 1000000 edges.")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(len(count1), len(count2), len(count3), len(count4), len(count5), "\n")



# Graphs with a randomly generated cycle of length 3 (small cycles)
graph500_small_cycle_dense = graph.graph_with_negative_cycle(500, 11200, 0, 3)
graph1000_small_cycle_dense = graph.graph_with_negative_cycle(1000, 31600, 0, 3)
graph2000_small_cycle_dense = graph.graph_with_negative_cycle(2000, 89000, 0, 3)
graph5000_small_cycle_dense = graph.graph_with_negative_cycle(5000, 354000, 0, 3)
graph10000_small_cycle_dense = graph.graph_with_negative_cycle(10000, 1000000, 0, 3)

# Experiment 4: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least a cycle of length 3.
# The number of edges is about N*square root(N). N is the number of vertices.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations.
counter_list1, counter_list2, counter_list3, counter_list4, counter_list5 = [], [], [], [], []
for _ in range(num_iterations):
    counter_list1 += [algorithms.negative_cycle_detection_modified(graph500_small_cycle_dense, 0)[3]]
    counter_list2 += [algorithms.negative_cycle_detection_modified(graph1000_small_cycle_dense, 0)[3]]
    counter_list3 += [algorithms.negative_cycle_detection_modified(graph2000_small_cycle_dense, 0)[3]]
    counter_list4 += [algorithms.negative_cycle_detection_modified(graph5000_small_cycle_dense, 0)[3]]
    counter_list5 += [algorithms.negative_cycle_detection_modified(graph10000_small_cycle_dense, 0)[3]]
average1, average2 = sum(counter_list1) / num_iterations, sum(counter_list2) / num_iterations
average3, average4 = sum(counter_list3) / num_iterations, sum(counter_list4) / num_iterations
average5 = sum(counter_list5) / num_iterations
count1 = [c for c in counter_list1 if c > 500 / 3]
count2 = [c for c in counter_list2 if c > 1000 / 3]
count3 = [c for c in counter_list3 if c > 2900 / 3]
count4 = [c for c in counter_list4 if c > 5000 / 3]
count5 = [c for c in counter_list5 if c > 10000 / 3]
print("When running the algorithm on graphs with at least one cycle of length 3 in each cycle and relatively dense,")
print("The average iterations to detect the negative cycle is: ")
print(average1, " when the graph consist of 500 vertices and 11200 edges,")
print(average2, " when the graph consist of 1000 vertices and 31600 edges,")
print(average3, " when the graph consist of 2000 vertices and 89000 edges,")
print(average4, " when the graph consist of 5000 vertices and 354000 edges,")
print(average5, " when the graph consist of 10000 vertices and 1000000 edges.")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(len(count1), len(count2), len(count3), len(count4), len(count5), "\n")


# Graphs with a randomly generated hamiltonian cycle in each graph (large cycles)
graph500_hamiltonian_full = graph.graph_with_negative_hamiltonian_cycle(500, 249500)
graph1000_hamiltonian_full = graph.graph_with_negative_hamiltonian_cycle(1000, 999000)
graph2000_hamiltonian_full = graph.graph_with_negative_hamiltonian_cycle(2000, 3998000)
graph5000_hamiltonian_full = graph.graph_with_negative_hamiltonian_cycle(5000, 24995000)

# Experiment 5: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least hamiltonian cycle.
# The number of edges is about N*square root(N). N is the number of vertices.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations
counter_list1, counter_list2, counter_list3, counter_list4, counter_list5 = [], [], [], [], []
for i in range(num_iterations):
    counter_list1 += [algorithms.negative_cycle_detection_modified(graph500_hamiltonian_full, 0)[3]]
    counter_list2 += [algorithms.negative_cycle_detection_modified(graph500_hamiltonian_full, 0)[3]]
    counter_list3 += [algorithms.negative_cycle_detection_modified(graph2000_hamiltonian_full, 0)[3]]
    counter_list4 += [algorithms.negative_cycle_detection_modified(graph5000_hamiltonian_full, 0)[3]]
average1, average2 = sum(counter_list1) / num_iterations, sum(counter_list2) / num_iterations
average3, average4 = sum(counter_list3) / num_iterations, sum(counter_list4) / num_iterations
count1 = [c for c in counter_list1 if c > 500 / 3]
count2 = [c for c in counter_list2 if c > 1000 / 3]
count3 = [c for c in counter_list3 if c > 2900 / 3]
count4 = [c for c in counter_list4 if c > 5000 / 3]
print("When running the algorithm on graphs with at least one hamiltonian cycle in each cycle and relatively dense,")
print("The average iterations to detect the negative cycle is: ")
print(average1, " when the graph consist of 500 vertices and 249500 edges,")
print(average2, " when the graph consist of 1000 vertices and 999000 edges,")
print(average3, " when the graph consist of 2000 vertices and 3998000 edges,")
print(average4, " when the graph consist of 5000 vertices and 24995000 edges,")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(len(count1), len(count2), len(count3), len(count4), "\n")

# Graphs with a randomly generated cycle of length 3 (small cycles)
graph500_small_cycle_full = graph.graph_with_negative_cycle(500, 249500, 0, 3)
graph1000_small_cycle_full = graph.graph_with_negative_cycle(1000, 999000, 0, 3)
graph2000_small_cycle_full = graph.graph_with_negative_cycle(2000, 3998000, 0, 3)
graph5000_small_cycle_full = graph.graph_with_negative_cycle(5000, 24995000, 0, 3)
# graph10000_small_cycle_full = graph.graph_with_negative_cycle(10000, 99990000, 0, 3)

# Experiment 6: find out the average iterations that is necessary for finding negative cycles if we run the subgraph traversal
# to find a cycle in the parent graph from the first iteration. Each graph contains at least a cycle of length 3.
# Check if the  algorithm can detect negative cycles after n/3 + o(n) iterations.
counter_list1, counter_list2, counter_list3, counter_list4, counter_list5 = [], [], [], [], []
for i in range(num_iterations):
    counter_list1 += [algorithms.negative_cycle_detection_modified(graph500_small_cycle_full, 0)[3]]
    counter_list2 += [algorithms.negative_cycle_detection_modified(graph1000_small_cycle_full, 0)[3]]
    counter_list3 += [algorithms.negative_cycle_detection_modified(graph2000_small_cycle_full, 0)[3]]
    counter_list4 += [algorithms.negative_cycle_detection_modified(graph5000_small_cycle_full, 0)[3]]
    # counter_list5 += [algorithms.negative_cycle_detection_modified(graph10000_small_cycle_full, 0)[3]]
average1, average2 = sum(counter_list1) / num_iterations, sum(counter_list2) / num_iterations
average3, average4 = sum(counter_list3) / num_iterations, sum(counter_list4) / num_iterations
# average5 = sum(counter_list5) / num_iterations
count1 = [c for c in counter_list1 if c > 500 / 3]
count2 = [c for c in counter_list2 if c > 1000 / 3]
count3 = [c for c in counter_list3 if c > 2900 / 3]
count4 = [c for c in counter_list4 if c > 5000 / 3]
# count5 = [c for c in counter_list5 if c > 10000 / 3]
print("When running the algorithm on graphs with at least one cycle of length 3 in each cycle and very dense,")
print("The average iterations to detect the negative cycle is: ")
print(average1, " when the graph consist of 500 vertices and 249500 edges,")
print(average2, " when the graph consist of 1000 vertices and 999000 edges,")
print(average3, " when the graph consist of 2000 vertices and 3998000 edges,")
print(average4, " when the graph consist of 5000 vertices and 24995000 edges,")
# print(average5, " when the graph consist of 10000 vertices and 99990000 edges.")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(len(count1), len(count2), len(count3), len(count4), "\n")

"""

# Graphs without any negative cycles.
graph500 = graph.graph_generator(500, 3100, False)
graph1000 = graph.graph_generator(1000, 6900, False)
graph2000 = graph.graph_generator(2000, 15000, False)
graph5000 = graph.graph_generator(5000, 42000, False)
graph10000 = graph.graph_generator(10000, 92000, False)

graph500_dense = graph.graph_generator(500, 11200, False)
graph1000_dense = graph.graph_generator(1000, 31600, False)
graph2000_dense = graph.graph_generator(2000, 89000, False)
graph5000_dense = graph.graph_generator(5000, 354000, False)
graph10000_dense = graph.graph_generator(10000, 1000000, False)

graph500_full = graph.graph_generator(500, 249500, False)
graph1000_full = graph.graph_generator(1000, 999000, False)
graph2000_full = graph.graph_generator(2000, 3998000, False)
graph5000_full = graph.graph_generator(5000, 24995000, False)

counter_list1, counter_list2, counter_list3, counter_list4, counter_list5 = [], [], [], [], []
for _ in range(num_iterations):
    counter_list1 += [algorithms.negative_cycle_detection_modified(graph500, 0)[3]]
    counter_list2 += [algorithms.negative_cycle_detection_modified(graph1000, 0)[3]]
    counter_list3 += [algorithms.negative_cycle_detection_modified(graph2000, 0)[3]]
    counter_list4 += [algorithms.negative_cycle_detection_modified(graph5000, 0)[3]]
    counter_list5 += [algorithms.negative_cycle_detection_modified(graph10000, 0)[3]]
average1, average2 = sum(counter_list1) / num_iterations, sum(counter_list2) / num_iterations
average3, average4 = sum(counter_list3) / num_iterations, sum(counter_list4) / num_iterations
average5 = sum(counter_list5) / num_iterations
count1 = [c for c in counter_list1 if c > 500 / 3]
count2 = [c for c in counter_list2 if c > 1000 / 3]
count3 = [c for c in counter_list3 if c > 2900 / 3]
count4 = [c for c in counter_list4 if c > 5000 / 3]
count5 = [c for c in counter_list5 if c > 10000 / 3]
print("When running the algorithm on graphs without negative cycles in each cycle and sparse,")
print("The average iterations to detect the negative cycle is: ")
print(average1, " when the graph consist of 500 vertices and 3100 edges,")
print(average2, " when the graph consist of 1000 vertices and 6900 edges,")
print(average3, " when the graph consist of 2000 vertices and 15000 edges,")
print(average4, " when the graph consist of 5000 vertices and 42000 edges,")
print(average5, " when the graph consist of 10000 vertices and 92000 edges.")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(len(count1), len(count2), len(count3), len(count4), len(count5), "\n")


counter_list1, counter_list2, counter_list3, counter_list4, counter_list5 = [], [], [], [], []
for _ in range(num_iterations):
    counter_list1 += [algorithms.negative_cycle_detection_modified(graph500_dense, 0)[3]]
    counter_list2 += [algorithms.negative_cycle_detection_modified(graph1000_dense, 0)[3]]
    counter_list3 += [algorithms.negative_cycle_detection_modified(graph2000_dense, 0)[3]]
    counter_list4 += [algorithms.negative_cycle_detection_modified(graph5000_dense, 0)[3]]
    counter_list5 += [algorithms.negative_cycle_detection_modified(graph10000_dense, 0)[3]]
average1, average2 = sum(counter_list1) / num_iterations, sum(counter_list2) / num_iterations
average3, average4 = sum(counter_list3) / num_iterations, sum(counter_list4) / num_iterations
average5 = sum(counter_list5) / num_iterations
count1 = [c for c in counter_list1 if c > 500 / 3]
count2 = [c for c in counter_list2 if c > 1000 / 3]
count3 = [c for c in counter_list3 if c > 2900 / 3]
count4 = [c for c in counter_list4 if c > 5000 / 3]
count5 = [c for c in counter_list5 if c > 10000 / 3]
print("When running the algorithm on graphs without negative cycles in each cycle and dense,")
print("The average iterations to detect the negative cycle is: ")
print(average1, " when the graph consist of 500 vertices and 3100 edges,")
print(average2, " when the graph consist of 1000 vertices and 6900 edges,")
print(average3, " when the graph consist of 2000 vertices and 15000 edges,")
print(average4, " when the graph consist of 5000 vertices and 42000 edges,")
print(average5, " when the graph consist of 10000 vertices and 92000 edges.")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(len(count1), len(count2), len(count3), len(count4), len(count5), "\n")


counter_list1, counter_list2, counter_list3, counter_list4 = [], [], [], []
for _ in range(num_iterations):
    counter_list1 += [algorithms.negative_cycle_detection_modified(graph500_full, 0)[3]]
    counter_list2 += [algorithms.negative_cycle_detection_modified(graph1000_full, 0)[3]]
    counter_list3 += [algorithms.negative_cycle_detection_modified(graph2000_full, 0)[3]]
    counter_list4 += [algorithms.negative_cycle_detection_modified(graph5000_full, 0)[3]]
    # counter_list5 += [algorithms.negative_cycle_detection_modified(graph10000_full, 0)[3]]
average1, average2 = sum(counter_list1) / num_iterations, sum(counter_list2) / num_iterations
average3, average4 = sum(counter_list3) / num_iterations, sum(counter_list4) / num_iterations
average5 = sum(counter_list5) / num_iterations
count1 = [c for c in counter_list1 if c > 500 / 3]
count2 = [c for c in counter_list2 if c > 1000 / 3]
count3 = [c for c in counter_list3 if c > 2900 / 3]
count4 = [c for c in counter_list4 if c > 5000 / 3]
# count5 = [c for c in counter_list5 if c > 10000 / 3]
print("When running the algorithm on graphs without negative cycles in each cycle and full,")
print("The average iterations to detect the negative cycle is: ")
print(average1, " when the graph consist of 500 vertices and 3100 edges,")
print(average2, " when the graph consist of 1000 vertices and 6900 edges,")
print(average3, " when the graph consist of 2000 vertices and 15000 edges,")
print(average4, " when the graph consist of 5000 vertices and 42000 edges,")
# print(average5, " when the graph consist of 10000 vertices and 92000 edges.")
print("The numbers of tests that use more that n / 3 iterations to detect negative cycles are:")
print(len(count1), len(count2), len(count3), len(count4), "\n")