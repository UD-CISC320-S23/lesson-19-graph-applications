import networkx as nx
import matplotlib.pyplot as plt

# Initialize the graph
possible_destinations = nx.DiGraph()

# Add each destination as a vertex on the graph
stops_as_nodes = open("train_stops.txt")
stops_as_nodes = stops_as_nodes.read().split()
for node in stops_as_nodes:
    possible_destinations.add_node(node)

# Add each train track/route as an edge in the graph
stops_as_edges = open("train_routes.txt")
stops_as_edges = stops_as_edges.read().split()
i = 0
for edge in stops_as_edges:
    stops_as_edges[i] = edge.split(",")
    i+=1
for edge in stops_as_edges:
    possible_destinations.add_edge(edge[0],edge[1])

# Create a visualization of the graph
pos = nx.circular_layout(possible_destinations)
plt.figure(20,figsize=(12,12))
nx.draw_networkx_edges(possible_destinations, pos)
nx.draw_networkx(possible_destinations,pos, node_size=100, font_size=16)
plt.savefig("graph_for_bfs.png")
# Output the result
for destination in possible_destinations:
    print(destination + ": ", end="")
    connected_stops = dict(nx.bfs_successors(possible_destinations, destination))
    for stop in connected_stops:
        print(",".join(list(connected_stops[stop])) + ",", end="")
    print()