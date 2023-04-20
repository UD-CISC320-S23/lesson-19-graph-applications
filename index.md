# Resturants in Newark

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Heni Patel (heni@udel.edu)
* Christopher Bennett (cbcolleg@udel.edu)
* Ella Wilkins (ellawlk@udel.edu)
* Sneha Nangelimalil (snehnang@udel.edu)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# Probelm #2: Lowest Delivery Cost

**Informal Description**: 
There is a wedding party that wants to have food from all 20 restaurants. But, the wedding is
in four hours and they do not have enough time or money to pick up all the food. The wedding part is hiring 
a food delivery service to go to every restaurant and pick up the food. The cost changes depending
on what order the delivery driver goes too. The wedding party is trying to find the minimal cost
to collect the food from all the restaurants. Below is the restaurant path that will give the minimal cost.

> **Formal Description**:
A Prims algorithm minimum spanning tree will be used to find the lowest cost for the delivery driver to
go to the 20 restuarant and pick up the food. The algorithm will find the lowest cost between each 
restaurant and take that path.
>  * Input: A connected undirected graph G = (V, E) of resturants with edge weights that represent the cost of distance traveled.
>  * Output: A minimal spanning tree representing the path that will give the lowest cost to pick up all the food from each restaurant. 

**Graph Problem/Algorithm**: MST


**Setup code**:

```
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

#print("G.nodes = ", G.nodes)
#print("G.edges = ", G.edges)
#print("G.degree = ", G.degree)
#print("G.adj = ", G.adj)

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
```

**Visualization**:

![Prims Graph](prims_graph1.png)

**Solution code:**

```
mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
sorted(sorted(e) for e in edgelist)
print(edgelist)
```

**Output**

```
[('Caffe Gelato', "Mama's Pizza & Pasta"), ("Mama's Pizza & Pasta", 'Oishii Sushi & Ramen'), ("Mama's Pizza & Pasta", 'Santa Fe'), ('Santa Fe', 'May Flower'), ('May Flower', 'El Diablo'), ('Oishii Sushi & Ramen', 'Deer Park Tavern'), ('El Diablo', 'Home Grown'), ('Oishii Sushi & Ramen', 'Indian Sizzler'), ('Home Grown', 'm2o Burgers'), ('m2o Burgers', "Klondike Kate's"), ("Klondike Kate's", 'Snap Custom Pizza'), ('Snap Custom Pizza', 'Playa Bowls'), ('Playa Bowls', '2SPizza'), ('2SPizza', 'Five Guys'), ('Five Guys', 'Taverna Newark'), ('El Diablo', 'QDOBA'), ('El Diablo', 'Honey Grow'), ('Honey Grow', 'Roots'), ('Roots', "Hamilton's")]
```

**Interpretation of Results**: