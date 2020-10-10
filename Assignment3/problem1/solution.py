# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262

line_input = list(map(int, input().split()))
num_vertices = line_input[0]
num_edges = line_input[1]

graph = []
r_graph = []
visited = [] 
pre = []
post = []
postlist = [] 
magic_order = []
num_cc = 0

for i in range(num_vertices):
    visited.append(0)
    pre.append(0)
    post.append(0)
    
for i in range(num_vertices):
    graph.append([])
    r_graph.append([])

for i in range(num_edges):
    n, m = list(map(int, input().split()))
    graph[n-1].append(m)
    r_graph[m-1].append(n) # Build reversed graph.
    
clock = 1
def DFS_time(graph):
    global num_vertices
    global clock 
    global visited 
    clock = 1
    for i in range(num_vertices):
        if (visited[i] == 0):
            explore(graph, i)
    

def explore(graph, v):
    global visited
    global pre 
    global post
    global postlist 
    global clock
    visited[v] = 1
    pre[v] = clock
    clock += 1
    for each in graph[v]:
        if (visited[each-1] == 0):
            explore(graph,each-1)
    post[v] = clock
    clock += 1
    postlist.append(v)

def specific_order(graph):
    global magic_order
    global r_graph
    global postlist
    DFS_time(r_graph)
    postlist.reverse()
    magic_order = postlist

def explore_specific(graph, vi):
    global visited
    visited[vi] = num_cc
    for each in graph[vi]:
        if (visited[each-1] == 0):
            explore(graph,each-1)

def DFS_specific(graph):
    global num_cc
    num_cc = 0
    for vi in range(num_vertices):
        if (visited[vi] == 0):
            num_cc += 1
            explore_specific(graph, vi)

specific_order(graph)
for i in range(num_vertices):
    visited[i] = 0
DFS_specific(magic_order)
print(num_cc)