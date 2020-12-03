# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262
import sys

line_input = list(map(int, input().split(" ")))

# First line read
num_vertices = line_input[0]
num_edges = line_input[1]
source_vertex = line_input[2]

G = dict()

for i in range(1, num_vertices + 1):
    temp = dict()
    G[i] = temp
# graph = {'a': {'b': 5, 'c': 2}, 'b': {'c': 1, 'd': 3},
#          'c': {'b': 3, 'd': 7}, 'd': {'e': 7}, 'e': {'d': 9}}

# Read the rest of the lines
for k in range(num_edges):
    line_input = list(map(int, input().split(" ")))
    # Edge (a,b) with length: length
    a = line_input[0]
    b = line_input[1]
    length = line_input[2]
    G[a][b] = length


def FindNegativeCycle(graph, source):
    global num_vertices
    dist = [sys.maxsize] * num_vertices
    prev = [None] * num_vertices
    dist[source - 1] = 0

    for k in range(num_vertices - 1):
        for v in range(num_vertices):
            for e in G[v+1]:
                if(dist[e-1] > dist[v] + G[v+1][e]):
                    dist[e-1] = dist[v] + G[v+1][e]
                    prev[e-1] = v + 1

    weUpdate = False

    for v in range(num_vertices):
        for e in G[v+1]:
            if(dist[e-1] > dist[v] + G[v+1][e]):
                dist[e-1] = dist[v] + G[v+1][e]
                prev[e-1] = v + 1
                weUpdate = True

    if weUpdate:
        return True
    else:
        return False


output = FindNegativeCycle(G, source_vertex)

if output:
    print("True")
else:
    print("False")
