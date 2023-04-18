#test file for prims. i used same method for loading data as in previous lessons.
import networkx as nx
import matplotlib.pyplot as plt
if __name__ == '__main__':
    edges = []
    with open("tourist_destinations.txt") as data_file:
        lines: list[str]
        lines = data_file.readlines()

    edgeList = lines[1:]
    destinations = nx.Graph()
    for edge in edgeList:
        edges.append(edge.split(","))
    for edge in edges:
        test = edge[2]
        destinations.add_edge(edge[0], edge[1], weight=int(edge[2]))

    pos = nx.circular_layout(destinations)
    plt.figure(20,figsize=(12,12))
    labels = nx.get_edge_attributes(destinations,'weight')
    nx.draw_networkx(destinations,pos, node_size=100, font_size=16)
    nx.draw_networkx_edge_labels(destinations,pos,edge_labels=labels)
    plt.savefig("graph_for_prims.png")