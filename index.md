# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Rohan Yarlagadda (rohany@udel.edu)
* Second member (email)
* Third member (email)
* Fourth member (email)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
import matplotlib.pyplot as plt
```

# Prim's Algorithm

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: MST (Prims)


**Setup code**:

```python
g = nx.Graph()
g.add_edge("Frazer Field", "Lil Bob", weight = 1)
g.add_edges_from([("Lil Bob", "Taylor"), ("Lil Bob", "Old College"), ("Lil Bob", "Brown Hall")], weight = 3)
g.add_edges_from([("Willard Hall", "McDowell Hall"), ("Willard Hall", "Old College"), ("Willard Hall", "Trabant")], weight = 2)
g.add_edge("Taylor", "Old College", weight = 1)
g.add_edges_from([("Brown Hall", "Harter"), ("Brown Hall", "Sypherd"), ("Brown Hall", "Sharp Hall")], weight = 1)
g.add_edges_from([("Harter", "Sypherd"), ("Harter", "Sharp Hall")], weight = 1)
g.add_edges_from([("Trabant", "Kirkbride"), ("Trabant", "Sharp Lab"), ("Trabant", "Ewing")], weight = 3)
g.add_edges_from([("Kirkbride", "Ewing"), ("Kirkbride", "Purnell"), ("Kirkbride", "Smith")], weight = 1)
g.add_edges_from([("Ewing", "Purnell"), ("Ewing", "Smith")], weight = 1)
g.add_edge("Purnell", "Smith", weight = 1)
g.add_edges_from([("Sharp Lab", "Wolf"), ("Sharp Lab", "Gore")], weight = 2)
g.add_edges_from([("Gore", "Mitchell"), ("Gore", "Memorial"), ("Gore", "Brown Lab"), ("Gore", "Smith")], weight = 2)
g.add_edges_from([("Brown Lab", "Colburn"), ("Brown Lab", "ICE")], weight = 4)
g.add_edges_from([("Morris", "Memorial"), ("Morris", "Allison"), ("Morris", "Perkins")], weight = 3)
g.add_edges_from([("Perkins", "Redding"), ("Perkins", "Russel"), ("Perkins", "Harrington")], weight = 3)
g.add_edges_from([("Harrington", "Russel"), ("Harrington", "Redding")], weight = 2)
g.add_edge("Redding", "Russel", weight = 2)
g.add_edges_from([("ICE", "Penny"), ("ICE", "Colburn"), ("ICE", "Spencer Lab")], weight = 3)
g.add_edge("Spencer Lab", "Colburn", weight = 2)
g.add_edges_from([("Allison", "Perkins"), ("Allison", "Penny")], weight = 4)

pos = nx.spring_layout(g)
nx.draw(g, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
plt.show()
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
Prim_path = nx.minimum_spanning_tree(locationGraph.g, weight='weight', algorithm='prim', ignore_nan=False)
pos = nx.spring_layout(Prim_path)
nx.draw(Prim_path, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(Prim_path, 'weight')
nx.draw_networkx_edge_labels(Prim_path, pos, edge_labels=edge_labels)
plt.show()
```

**Output**

```
```

**Interpretation of Results**:

# Second Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:

# Third Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:

