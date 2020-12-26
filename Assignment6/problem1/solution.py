# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262
import queue as q
import sys as s


class Edge:
    def __init__(self, capacity, flow):
        self.flow = flow
        self.capacity = capacity


class GrEdge:
    def __init__(self, weight, isBack):
        self.weight = weight
        self.isBack = isBack


line_input = list(map(int, input().split(" ")))

# First line read
num_vertices = line_input[0]
num_edges = line_input[1]

G = dict()
Gr = dict()

# G[1] = source. G[num_vertices] = sink
for i in range(1, num_vertices + 1):
    temp1 = dict()
    temp2 = dict()
    G[i] = temp1
    Gr[i] = temp2
# graph = {'a': {'b': (Edge)}, 'c': 2}, 'b': {'c': 1, 'd': 3},
#          'c': {'b': 3, 'd': 7}, 'd': {'e': 7}, 'e': {'d': 9}}

# Read the rest of the lines
for k in range(num_edges):
    line_input = list(map(int, input().split(" ")))
    # Edge (a,b) with capacity: length
    a = line_input[0]
    b = line_input[1]
    edge = Edge(line_input[2], 0)  # no flow all capacity

    if a in G and b in G[a]:
        G[a][b].capacity += edge.capacity
    else:
        G[a][b] = edge


def is_connected():  # Find a path from s to t in the residual graph
    global Gr
    sink = num_vertices
    explored = []

    # Add the source vertex to the queue
    queue = [[1]]

    # Loop until the queue is empty
    while queue:
        # Start by poping the top of the queue and set v to teh end of the path
        u = queue.pop(0)
        v = u[-1]

        # Only check unexplored vertices
        if v not in explored:
            adjacent = Gr[v]

            # Loop through the adjacent vertices
            for vertex in adjacent:
                nextPath = list(u)
                nextPath.append(vertex)
                queue.append(nextPath)

                # If we find the sink vertex, we find the know there is a path
                if vertex == sink:
                    return nextPath
            # add the vertex into the explored list
            explored.append(v)

    return None


def find_max_flow():
    global Gr, G

    # build the residual graph, which is just G when theres no flow
    for i in range(1, num_vertices + 1):
        for edge in G[i]:
            # Forward edge for available capacity, backward edge for used
            if G[i][edge].capacity - G[i][edge].flow > 0:  # make forward edge
                gredge = GrEdge(G[i][edge].capacity - G[i][edge].flow, False)
                Gr[i][edge] = gredge

    path = is_connected()
    # Loop until we cant find a path
    while(path != None):

        # Augment Reality
        minEdge = s.maxsize  # set the min to system max int
        for k in range(len(path) - 1):
            if(Gr[path[k]][path[k+1]].weight < minEdge):
                minEdge = Gr[path[k]][path[k+1]].weight

        for k in range(len(path) - 1):
            # We are a forward edge
            if path[k] in G and path[k+1] in G[path[k]] and not Gr[path[k]][path[k+1]].isBack:
                G[path[k]][path[k+1]].flow += minEdge
            elif path[k + 1] in G and path[k] in G[path[k + 1]] and Gr[path[k]][path[k+1]].isBack:
                G[path[k + 1]][path[k]].flow -= minEdge

        # build the residual graph
        for i in range(1, num_vertices + 1):
            for edge in G[i]:
                # Forward edge for available capacity, backward edge for used
                if G[i][edge].capacity - G[i][edge].flow > 0:  # make forward edge
                    gredge = GrEdge(G[i][edge].capacity -
                                    G[i][edge].flow, False)
                    Gr[i][edge] = gredge
                else:
                    if edge in Gr[i] and not Gr[i][edge].isBack:
                        del Gr[i][edge]
                if G[i][edge].flow > 0:  # Backward Edge
                    gredge = GrEdge(G[i][edge].flow, True)
                    Gr[edge][i] = gredge
                else:
                    if i in Gr[edge] and Gr[edge][i].isBack:
                        del Gr[edge][i]
        path = is_connected()

    return


find_max_flow()
# We gonna print the sum of the out edges of G[1] for the output i think
max_flow = 0
for edgeConnection in G[1]:
    max_flow += G[1][edgeConnection].flow

print(max_flow)
