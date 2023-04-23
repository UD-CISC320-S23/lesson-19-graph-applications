import networkx as nx
import locationGraph
import matplotlib.pyplot as plt

pathway = nx.dfs_edges(locationGraph.g, source=None, depth_limit=None)
dfsTree = nx.dfs_tree(locationGraph.g,source=None,depth_limit=None)


