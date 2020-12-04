# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262
import sys

class Node():
    def __init__(self, data, height, parent):
        self.data = data
        self.height = height
        self.parent = parent

line_input = list(map(int, input().split(" ")))

# Reads
num_vertices = line_input[0]
num_edges = line_input[1]

edge_weights = []

# Save edge weights in a list
for i in range(1, num_edges + 1):
    line_input = list(map(int, input().split(" ")))
    start_vertex = line_input[0]
    end_vertex = line_input[1]
    edge_weights.append(line_input[2])

# Sort edge weights
# print(edge_weights)
edge_weights.sort()

E1 = []

def make_set(v):
    v.height = 1;
    v.parent = v;

def find(v):
    while (v.parent != v):
        v = v.parent
    return v

for v in range(num_vertices + 1):
    make_set(v)