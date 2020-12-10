# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262
import sys


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class Set:

    def __init__(self, vertex):
        self.height = 1
        self.parent = self
        self.vertex = vertex

    def find(self):
        current = self
        while (current.parent != current):
            current = current.parent
        return current


def union(x, y):
    rx = x.find()
    ry = y.find()

    if(rx == ry):
        return

    if(rx.height < ry.height):
        rx.parent = ry
    elif rx.height > ry.height:
        ry.parent = rx
    else:
        rx.parent = ry
        ry.height = ry.height + 1

    return


line_input = list(map(int, input().split(" ")))

# Reads
num_vertices = line_input[0]
num_edges = line_input[1]

edges = []
# Save edge weights in a list
for i in range(1, num_edges + 1):
    line_input = list(map(int, input().split(" ")))
    edges.append(Edge(line_input[0], line_input[1], line_input[2]))

# Sort edge weights
# print(edge_weights)
edges.sort()

E1 = []
vertex_set = []
vertex_set.append(None)

for v in range(1, num_vertices + 1):
    vertex_set.append(Set(v))

for e in edges:
    # Find root of u
    start_root = vertex_set[e.start].find()
    end_root = vertex_set[e.end].find()

    if(start_root != end_root):
        E1.append(e)
        union(start_root, end_root)

total = 0
# Add up the MST weights
for edgeee in E1:
    total += edgeee.weight

print(total)
