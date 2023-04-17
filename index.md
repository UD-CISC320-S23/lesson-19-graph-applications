# Transportations

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Paul Kearney (paulke@udel.edu)
* Second member (email)
* Third member (email)
* Fourth member (email)

Description of project

Our project heavily revolves around modes of transportation. This is what we all gravitated towards when we were thinking
of real world applications of graphing algorithms. 

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# busing in CA
**Informal Description**: 
A tour bus company based in LA wants to map out new routes and want to stop as often as possible to
pick up new travelers, but also stop at every popular tourist destination. in order to do this, the bussing 
company wants to pick routes such that the bus drives on the shortest road to get to each location.
> **Formal Description**:
>  * Input: An undirected graph of tourist destinations. edges being roads that connect destinations,vertices 
>  * the destinations themselves.
>  * Output: minimum spanning tree of tourist destinations

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]


**Setup code**:

```python
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
```
**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
solution = nx.minimum_spanning_tree(destinations,algorithm="prim",data=False)
print(solution.edges(data=True))

```

**Output**
edgelist = list(solution)
```
```

**Interpretation of Results**:

