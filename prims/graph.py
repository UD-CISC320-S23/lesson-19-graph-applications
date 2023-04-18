import networkx as nx
import matplotlib.pyplot as plt
import pprint
import json

"""
1.An informal description of the problem, written for intelligent non-Computer Scientists
There is a wedding party that wants to have food from all 20 restaurants. But, the wedding is
in four hours and they do not have enough time or money to pick up all the food. The wedding part is hiring 
a food delivery service to go to every restaurant and pick up the food. The cost changes depending
on what order the delivery driver goes too. The wedding party is trying to find the minimal cost
to collect the food from all the restaurants. Below is the restaurant path that will give the minimal cost.

2.A formal description of the problem, written for other Computer Scientists

3.Which of the four main graph problems you are solving (MST)

4.A visualization of the graph for the problem
5.The syntax-highlighted code used to load the data into `networkx` and to call the appropriate graph algorithm function
6.The preformatted output of the graph algorithm function
7.An interpretation of the results that meaningfully answer the question
"""
#Create empty undirected graph
G = nx.Graph()

#Add edges
G.add_edge("Santa Fe", "May Flower", weight=1.3)
G.add_edge("May Flower", "Five Guys", weight=10)
G.add_edge("Five Guys", "2SPizza", weight=6.5)
G.add_edge("2SPizza", "Playa Bowls", weight=1.9)
G.add_edge("Taverna Newark", "Five Guys", weight=2.4)
G.add_edge("Oishii Sushi & Ramen", "Deer Park Tavern", weight=3.7)
G.add_edge("Indian Sizzler", "Oishii Sushi & Ramen", weight=4.4)
G.add_edge("Indian Sizzler", "Deer Park Tavern", weight=6.7)
#G.add_edge("Indian Sizzler", "Mama's Pizza & Pasta", weight=5.0)
#G.add_edge("Indian Sizzler", "Honey Grow", weight=7.8)
G.add_edge("Taverna Newark", "Hamilton's", weight=9.3)
G.add_edge("Caffe Gelato", "m2o Burgers", weight=8.9)
G.add_edge("El Diablo", "Home Grown", weight=4.3)
G.add_edge("El Diablo", "Honey Grow", weight=9.0)
G.add_edge("m2o Burgers", "Home Grown", weight= 4.6)
G.add_edge("Honey Grow", "Roots", weight=3.1)
G.add_edge("Klondike Kate's", "Snap Custom Pizza", weight=6.5)
G.add_edge("2SPizza", "Snap Custom Pizza", weight=3.4)
G.add_edge("Klondike Kate's", "m2o Burgers", weight=2.9)
G.add_edge("QDOBA", "Mama's Pizza & Pasta", weight=7.8)
G.add_edge("El Diablo", "May Flower", weight=2.4)
G.add_edge("May Flower", "Roots", weight=9.2)
G.add_edge("Santa Fe", "Mama's Pizza & Pasta", weight=2.3)
G.add_edge("Santa Fe", "El Diablo", weight=6.4)
G.add_edge("Caffe Gelato", "Mama's Pizza & Pasta", weight=5.1)
G.add_edge("El Diablo", "2SPizza", weight=8.3)
G.add_edge("Deer Park Tavern", "Santa Fe", weight=7.6)
G.add_edge("QDOBA", "Home Grown", weight=7.9)
G.add_edge("Roots", "Hamilton's", weight=5.7)
G.add_edge("Playa Bowls", "Snap Custom Pizza", weight=0.5)
G.add_edge("QDOBA", "El Diablo", weight=6.6)
G.add_edge("Oishii Sushi & Ramen", "Mama's Pizza & Pasta", weight=1.9)

print("Number of nodes = ", G.number_of_nodes())
print("Number of edges = ", G.number_of_edges())

print("G.nodes = ", G.nodes)
print("G.edges = ", G.edges)
print("G.degree = ", G.degree)
print("G.adj = ", G.adj)

#To visualize
#nx.draw_networkx(G)
plt.figure(1)
pos=nx.spring_layout(G, iterations=6000)
nx.draw_networkx(G, pos, arrows=False, with_labels=True)

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.02)
plt.axis("off")
plt.tight_layout()
plt.show()

#dist = nx.floyd_warshall(g)

#pprint.pprint(json.loads(json.dumps(dist)))

#Reference 
#https://www.youtube.com/watch?v=CPQeSmDGiOQ
#https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html


#if __name__ == "__main__":
 #   prims_graph()

#Add nodes
#G.add_node("Santa Fe")
#G.add_node("May Flower")
#G.add_node("Five Guys")
#G.add_node("Taverna Newark")
# G.add_node("Hamilton's")
# G.add_node("Caffe Gelato")
# G.add_node("El Diablo")
# G.add_node("Honey Grow")
# G.add_node("Home Grown Cafe")
# G.add_node("Roots")
# G.add_node("Klondike Kate's Restaurant & Saloon")
# G.add_node("m2o Burgers & Salads")
# G.add_node("QDOBA Mexican Eats")
# G.add_node("Mama's Pizza & Pasta")
# G.add_node("Indian Sizzler")
# G.add_node("2SPizza")
# G.add_node("Snap Custom Pizza and Salads")
# G.add_node("Playa Bowls")
# G.add_node("Deer Park Tavern")
# G.add_node("Oishii Sushi & Ramen")

#G.add_edge("Playa Bowls", "Oishii Sushi & Ramen")