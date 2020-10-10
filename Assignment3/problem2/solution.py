# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262
import queue as q
import sys as s

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


def Dijkstra(graph, source):
    global num_vertices
    dist = []
    prev = []
    priorityQueue = q.PriorityQueue()
    # Initialize all of THE values for distance to be -1, and prev to be None/NULL indicating unreachable
    for i in range(1, num_vertices + 1):
        dist.append(s.maxsize)
        prev.append(None)
        # PQ gets value of infinite priority and vertex (priority, vertex)
        priorityQueue.put((s.maxsize, i))

    dist[source - 1] = 0  # distance to itself is 0
    priorityQueue.put((0, source))  # Decrease the key value to 0
    while(priorityQueue.empty() == False):
        (x, u) = priorityQueue.get()
        for v in G[u]:
            if(dist[v - 1] > dist[u - 1] + G[u][v]):
                dist[v - 1] = dist[u - 1] + G[u][v]
                prev[v - 1] = u
                priorityQueue.put((dist[v - 1], v))

    return dist


# It gon be a list of the distances from s to i
output = Dijkstra(G, source_vertex)

for each in output:
    if(each == s.maxsize):
        print(-1)
    else:
        print(each)
