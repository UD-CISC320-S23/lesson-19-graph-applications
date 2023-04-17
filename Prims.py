#Python file for prims algorithm for lesson 19

import networkx as nx

g = nx.Graph()
g.add_edge("A", "B", weight = 4)
g.add_edge("B", "D", weight = 2)
f = nx.shortest_path(g, "A", "D", weight = "weight")
print(f)