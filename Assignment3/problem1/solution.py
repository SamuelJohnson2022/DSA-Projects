# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262

line_input = list(map(int, input().split()))
num_vertices = line_input[0]
num_edges = line_input[1]

graph = []

for i in range(num_edges):
    n, m = list(map(int, input().split()))
    print(n, m)
    

reversed_graph = []

def specificOrder(graph):
    # Build Gr
    for i in range(num_edges):
        for j in range(2):
            # swap vertices
            reversed_graph[i][j] = graph[i][j+1]
            reversed_graph[i][j+1] = graph[i][j]

            # Run DFS on reversed_graph => post_list
            # specific_order = post_list.reverse()
            # return specific_order

