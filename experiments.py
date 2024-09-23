import graph
import algorithms
import example_graphs

counter1, counter2, counter3, counter4, counter5 = 0, 0, 0, 0, 0
num_iterations = 1000
for _ in range(num_iterations):
    if(algorithms.adaptive_bellman_Ford(example_graphs.graph500, 0, 2)[3] == 1):
        counter1 += 1
    if(algorithms.adaptive_bellman_Ford(example_graphs.graph1000, 0, 2)[3] == 1):
        counter2 += 1
    if(algorithms.adaptive_bellman_Ford(example_graphs.graph2000, 0, 2)[3] == 1):
        counter3 += 1
    if(algorithms.adaptive_bellman_Ford(example_graphs.graph5000, 0, 2)[3] == 1):
        counter4 += 1
    if(algorithms.adaptive_bellman_Ford(example_graphs.graph10000, 0, 2)[3] == 1):
        counter5 += 1
prob1, prob2, prob3, prob4, prob5 = counter1 / num_iterations, counter2 / num_iterations, counter3 / num_iterations, counter4 / num_iterations, counter5 / num_iterations
print("The probability to detect the negative cycle after running the cycle detection of parent graph once is: ")
print(prob1 + "% when the graph consist of 500 vertices and 3100 edges,")
print(prob2 + "% when the graph consist of 1000 vertices and 6900 edges,")
print(prob3 + "% when the graph consist of 2000 vertices and 15000 edges,")
print(prob4 + "% when the graph consist of 5000 vertices and 42000 edges,")
print(prob5 + "% when the graph consist of 10000 vertices and 92000 edges.")