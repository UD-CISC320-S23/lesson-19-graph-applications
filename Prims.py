#Python file for prims algorithm for lesson 19
#Python file for prims algorithm for lesson 19
import networkx as nx
import locationGraph
import matplotlib.pyplot as plt

# prims_path = nx.minimum_spanning_edges(locationGraph.g, algorithm="prim", weight="weight")
# pos = nx.spring_layout(prims_path)
# nx.draw(prims_path, pos, with_labels=True)
# edge_labels = nx.get_edge_attributes(prims_path, 'weight')
# nx.draw_networkx_edge_labels(prims_path, pos, edge_labels=edge_labels)
# plt.show()
# # lst = list(prims_path)
# # print(lst)

Prim_path = nx.minimum_spanning_tree(locationGraph.g, weight='weight', algorithm='prim', ignore_nan=False)
pos = nx.spring_layout(Prim_path)
nx.draw(Prim_path, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(Prim_path, 'weight')
nx.draw_networkx_edge_labels(Prim_path, pos, edge_labels=edge_labels)
plt.show()