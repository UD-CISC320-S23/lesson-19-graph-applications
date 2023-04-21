#Python file for prims algorithm for lesson 19
import networkx as nx
import locationGraph

prims_path = nx.minimum_spanning_edges(locationGraph.g, algorithm="prim", weight="weight")
lst = list(prims_path)
print(lst)