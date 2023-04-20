import networkx as nx
import matplotlib.pyplot as plt

# create a new undirected graph
G = nx.Graph()

# add 10 pilot nodes
for i in range(1, 11):
    G.add_node("P" + str(i), node_type="pilot")

# add 10 flight nodes
for i in range(1, 11):
    G.add_node("F" + str(i), node_type="flight")

# add edges between pilots and flights
# assuming that Pilot P1 conflicts with Flight F2, F5, F9
G.add_edge("P1", "F2")
G.add_edge("P1", "F5")
G.add_edge("P1", "F9")

# assuming that Pilot P2 conflicts with Flight F1, F3, F6
G.add_edge("P2", "F1")
G.add_edge("P2", "F3")
G.add_edge("P2", "F6")

# assuming that Pilot P3 conflicts with Flight F2, F4, F7
G.add_edge("P3", "F2")
G.add_edge("P3", "F4")
G.add_edge("P3", "F7")

# assuming that Pilot P4 conflicts with Flight F1, F5, F8
G.add_edge("P4", "F1")
G.add_edge("P4", "F5")
G.add_edge("P4", "F8")

# assuming that Pilot P5 conflicts with Flight F3, F6, F9
G.add_edge("P5", "F3")
G.add_edge("P5", "F6")
G.add_edge("P5", "F9")

# assuming that Pilot P6 conflicts with Flight F4, F7, F10
G.add_edge("P6", "F4")
G.add_edge("P6", "F7")
G.add_edge("P6", "F10")

# assuming that Pilot P7 conflicts with Flight F1, F8, F10
G.add_edge("P7", "F1")
G.add_edge("P7", "F8")
G.add_edge("P7", "F10")

# assuming that Pilot P8 conflicts with Flight F2, F6, F10
G.add_edge("P8", "F2")
G.add_edge("P8", "F6")
G.add_edge("P8", "F10")

# assuming that Pilot P9 conflicts with Flight F3, F7, F9
G.add_edge("P9", "F3")
G.add_edge("P9", "F7")
G.add_edge("P9", "F9")

# assuming that Pilot P10 conflicts with Flight F4, F5, F10
G.add_edge("P10", "F4")
G.add_edge("P10", "F5")
G.add_edge("P10", "F10")

# create a layout for the graph and draw it
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=["red" if n[1]["node_type"] == "pilot" else "lightblue" for n in G.nodes(data=True)])

# Save the graph locally
plt.savefig("BFS_graph.png")

# check if the graph is bipartite
is_bipartite = nx.is_bipartite(G)
if is_bipartite:
    print("The graph is bipartite.")
    print("The minimum number of pilots required for the flights is")
else:
    print("The graph is not bipartite.")