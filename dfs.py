import networkx as nx
import matplotlib.pyplot as plt

# Initializes the graph
tierGraph = nx.DiGraph()

# Adds each tier vertex on the graph reading from the node file
tier_nodes = open("rewards_tiers.txt")
tier_nodes = tier_nodes.read().split()

for node in tier_nodes:
    tierGraph.add_node(node)

# Add each edge in the graph from another file in the form : node1 -> node2 = node1,node2
tier_edges = open("rewards_tiers_edges.txt")
tier_edges = tier_edges.read().split()
i = 0
for edge in tier_edges:
    tier_edges[i] = edge.split(",")
    i+=1
for edge in tier_edges:
    tierGraph.add_edge(edge[0],edge[1])

# Create a visualization of the graph
pos = nx.spring_layout(tierGraph)
plt.figure(15,figsize=(10,10))
nx.draw_networkx_edges(tierGraph, pos)
nx.draw_networkx(tierGraph,pos, node_size=100, font_size=15)
plt.savefig("graph_for_dfs.png")

for node in tierGraph:
    print(node + ": ", end="")
    node_connections = dict(nx.dfs_successors(tierGraph, node))
    for stop in node_connections:
        print(" -> ".join(list(node_connections[stop])) + " -> ", end="")
    print("\n")

print("------------------------------------------------------------------"+"\n")

# check for cycles in the graph
def find_cycles(graph):
    cycles = []
    visited = set()

    def dfs(node, path):
        visited.add(node)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                dfs(neighbor, path + [neighbor])
            elif neighbor == path[0]:
                cycles.append(path + [neighbor])

    for node in graph.nodes():
        dfs(node, [node])

    return cycles

cycles = find_cycles(tierGraph)

# print the cycles found
print("Cycles in the graph:")
for cycle in cycles:
    print(cycle)