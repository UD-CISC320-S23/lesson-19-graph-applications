import networkx as nx
import locationGraph

# Find shortest path from Willard Hall to Perkins
ans_path = nx.dijkstra_path(locationGraph.g, "Willard Hall", "Perkins")
print(f'To get from Willard to Perkins using the shortest path you need to follow this path:\n\t{ans_path}')