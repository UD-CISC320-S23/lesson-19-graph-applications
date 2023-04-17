import networkx as nx
#import matplotlib.pyplot as plt
import pprint
import json

#Create empty undirected graph
G = nx.Graph()

#Add nodes
G.add_node("Santa Fe")
G.add_node("May Flower")
G.add_node("Five Guys")

#Add edges
G.add_edge("Santa Fe", "May Flower")
G.add_edge("May Flower", "Five Guys")

print("Number of nodes = ", G.number_of_nodes())
print("Number of edges = ", G.number_of_edges())

print("G.nodes = ", G.nodes)
print("G.edges = ", G.edges)
print("G.degree = ", G.degree)
#print("G.adj = ", G.adj)