**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* First member (email)
* Second member (email)
* Third member (email)
* Fourth member (email)
* Ameer Abdelnasser (ameernas@udel.edu)
* Rohan Yarlagadda (rohany@udel.edu)
* Avinash Chouhan (avinashc@udel.edu)

Description of project

@@ -23,29 +22,49 @@ import networkx as nx
```

# First Problem Title

FIND COURSES NEEDED FOR BS COMPUTER SCIENCE MAJOR
**Informal Description**: 

Find courses needed problem: Iterates through all nodes and edges to find all the classes on the graph that a computer science student needs to take. This is important because if a student needs to know what classes to take, this graph and DFS algorithm shows the student the order of which classes to take.
> **Formal Description**:
>  * Input:
>  * Output:
**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]
**Graph Problem/Algorithm**: [DFS]


**Setup code**:

```python
```
class locationGraph: 
    import networkx as nx

    g = nx.Graph()
    g.add_edge("CISC108", "CISC181", weight = 1)
    g.add_edges_from([("CISC210", "CISC275"), ("CISC210", "CISC220"), ("CISC210", "CISC260")], weight = 3)
    g.add_edges("CISC108", "CISC210", weight = 2)
    g.add_edge("MATH210", "CISC320" weight = 3)
    g.add_edges_from([("CISC220", "CISC320"), ("CISC220", "CISC361"), ("CISC220", "CISC304"),("CISC220","CISC372")], weight = 1)
    g.add_edges_from([("CISC260", "CISC361"), ("CISC260", "CISC372")], weight = 1)
    g.add_edge("MATH241", "MATH210" weight = 4)
    g.add_edge("ENGL110", "ENGL410" weight = 5)
    g.add_edge("GEOL105L", "GEOL107" weight = 2)
    g.add_edge("GEOL105", "GEOL105L" weight = 1)
    g.add_edge("GEOL107", "GEOL107L" weight = 1)
    g.add_edge("CISC275", "CISC474" weight = 3)


**Visualization**:

![Image goes here](Relative image filename goes here)
![Image goes here] DFS-graph.png

**Solution code:**

```python
```
import networkx as nx
import locationGraph
import matplotlib.pyplot as plt

    pathway = nx.dfs_edges(locationGraph.g, source=None, depth_limit=None)
    dfsTree = nx.dfs_tree(locationGraph.g,source=None,depth_limit=None)


**Output**