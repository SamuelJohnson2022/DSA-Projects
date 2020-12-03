# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262
import sys

line_input = list(map(int, input().split(" ")))

# Reads
num_vertices = line_input[0]
num_edges = line_input[1]

edge_weights = []

for i in range(1, num_edges + 1):
    line_input = list(map(int, input().split(" ")))
    start_vertex = line_input[0]
    end_vertex = line_input[1]
    edge_weights.append(line_input[2])

print(edge_weights)

edge_weights.sort()

# sort edges in increasing order of weight
