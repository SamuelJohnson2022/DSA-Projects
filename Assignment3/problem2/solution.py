# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262

line_input = list(map(int, input().split(" ")))

# First line read
num_vertices = line_input[0]
num_edges = line_input[1]
source_vertex = line_input[2]

G = dict()

for i in range(num_vertices):
    temp = dict()
    G = {i: temp}
# graph = {'a': {'b': 5, 'c': 2}, 'b': {'c': 1, 'd': 3},
#          'c': {'b': 3, 'd': 7}, 'd': {'e': 7}, 'e': {'d': 9}}

print(G)

# Read the rest of the lines
for k in range(num_edges):
    line_input = list(map(int, input().split(" ")))
    # Edge (a,b) with length: length
    a = line_input[0]
    b = line_input[1]
    length = line_input[2]
    G[a][b] = length

print(G)


def Dijkstra(graph, source):
    return
