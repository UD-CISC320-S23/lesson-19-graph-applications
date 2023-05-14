import networkx as nx
import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Add nodes with labels A to V
for i in range(65, 87):
    G.add_node('Band ' + chr(i))

# Add edges to the graph
G.add_edge('Band A', 'Band F', weight=7)
G.add_edge('Band A', 'Band D', weight=5)
G.add_edge('Band B', 'Band C', weight=8)
G.add_edge('Band B', 'BandF', weight=9)
G.add_edge('Band B', 'Band E', weight=7)
G.add_edge('Band C', 'Band G', weight=5)
G.add_edge('Band D', 'Band F', weight=6)
G.add_edge('Band D', 'Band E', weight=15)
G.add_edge('Band E', 'Band F', weight=8)
G.add_edge('Band E', 'Band J', weight=9)
G.add_edge('Band F', 'Band G', weight=11)
G.add_edge('Band F', 'Band H', weight=8)
G.add_edge('Band G', 'Band I', weight=9)
G.add_edge('Band H', 'Band I', weight=7)
G.add_edge('Band H', 'Band L', weight=5)
G.add_edge('Band I', 'Band J', weight=6)
G.add_edge('Band I', 'Band L', weight=12)
G.add_edge('Band J', 'Band K', weight=10)
G.add_edge('Band K', 'Band L', weight=6)
G.add_edge('Band L', 'Band M', weight=8)
G.add_edge('Band M', 'Band N', weight=9)
G.add_edge('Band M', 'Band O', weight=10)
G.add_edge('Band N', 'Band P', weight=6)
G.add_edge('Band O', 'Band P', weight=7)
G.add_edge('Band O', 'Band S', weight=5)
G.add_edge('Band P', 'Band Q', weight=4)
G.add_edge('Band Q', 'Band R', weight=6)
G.add_edge('Band R', 'Band V', weight=9)
G.add_edge('Band S', 'Band T', weight=5)
G.add_edge('Band T', 'Band U', weight=7)
G.add_edge('Band U', 'Band V', weight=8)
G.add_edge('Band B', 'Band D', weight=3)
G.add_edge('Band C', 'Band F', weight=7)
G.add_edge('Band G', 'Band H', weight=5)
G.add_edge('Band I', 'Band K', weight=10)
G.add_edge('Band J', 'Band L', weight=4)
G.add_edge('Band M', 'Band R', weight=12)
G.add_edge('Band N', 'Band S', weight=8)
G.add_edge('Band O', 'Band T', weight=6)
G.add_edge('Band P', 'Band U', weight=9)
G.add_edge('Band Q', 'Band V', weight=11)
G.add_edge('Band L', 'Band S', weight=7)
G.add_edge('Band L', 'Band V', weight=10)
G.add_edge('Band L', 'Band A', weight=8)
G.add_edge('Band L', 'Band B', weight=9)
G.add_edge('Band A', 'Band G', weight=6)
G.add_edge('Band B', 'Band D', weight=10)
G.add_edge('Band C', 'Band H', weight=7)
G.add_edge('Band D', 'Band J', weight=8)
G.add_edge('Band E', 'Band K', weight=12)
G.add_edge('Band F', 'Band M', weight=13)
G.add_edge('Band G', 'Band N', weight=9)
G.add_edge('Band H', 'Band O', weight=11)
G.add_edge('Band I', 'Band P', weight=7)
G.add_edge('Band J', 'Band Q', weight=5)
G.add_edge('Band K', 'Band R', weight=9)
G.add_edge('Band L', 'Band S', weight=7)
G.add_edge('Band M', 'Band T', weight=6)
G.add_edge('Band N', 'Band U', weight=8)
G.add_edge('Band O', 'Band V', weight=10)

# Define edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')

# Compute the minimum spanning tree from node A to V
T = nx.algorithms.tree.minimum_spanning_tree(G.subgraph(nx.node_connected_component(G, 'Band A')), weight='weight')

# Draw the graph and tree
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='lightblue')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edges(T, pos, edge_color='red', width=2)
# plt.axis('off')
plt.show()

# plt.axis('off')
# plt.show()
# nx.draw(G)