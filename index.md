# UD course related graphs

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* First member (email)
* Second member (email)
* jfmarks@udel.edu
* Patrick Brady (pbrady@udel.edu)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# Using SSSP to find the easiest class

**Informal Description**:
Joe needs to figure out what the easiest path of prerequisites can be taken to get to ECON 490

> **Formal Description**:
>  * Input: 'ECON 101', 'ECON 490', and the ECON course graph
>  * Output: (['ECON 101', 'ECON 251', 'ECON 490'], 'weight = 4')

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]


**Setup code**:

```
    # the dictionary containing the adjacency for the graph
    adjacency_dict = {"ECON 101": [],
                      "ECON 103": ['ECON 101'],
                      "ECON 308": ['ECON 103'],
                      "ECON 251": ['ECON 101'],
                      "ECON 255": ['ECON 101'],
                      "ECON 300": ['ECON 101'],
                      "ECON 301": ['ECON 101'],
                      "ECON 303": ['ECON 103', 'ECON 251', 'ECON 255', 'ECON 300', 'ECON 301'],
                      "ECON 419": ['ECON 303'],
                      "ECON 304": ['ECON 103', 'ECON 301'],
                      "ECON 430": ['ECON 303', 'ECON 304'],
                      "ECON 435": ['ECON 303', 'ECON 304'],
                      "ECON 364": ['ECON 300', 'ECON 301'],
                      "ECON 408": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301'],
                      "ECON 418": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301'],
                      "ECON 426": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301'],
                      "ECON 433": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301'],
                      "ECON 436": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301', 'ECON 303', 'ECON 304'],
                      "ECON 441": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301'],
                      "ECON 443": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301', 'ECON 303', 'ECON 304'],
                      "ECON 444": ['ECON 251', 'ECON 300', 'ECON 301'],
                      "ECON 460": ['ECON 301'],
                      "ECON 463": ['ECON 251', 'ECON 300', 'ECON 301'],
                      "ECON 483": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301'],
                      "ECON 490": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301'],
                      "ECON 306": ['ECON 101', 'ECON 103'],
                      "ECON 406": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301', 'ECON 306'],
                      "ECON 410": ['ECON 251', 'ECON 255', 'ECON 300', 'ECON 301', 'ECON 306'],
                      "ECON 422": ['ECON 300', 'ECON 301', 'ECON 306'],
                      "ECON 423": ['ECON 422'],
                      "ECON 311": ['ECON 101', 'ECON 103'],
                      "ECON 315": ['ECON 101', 'ECON 103'],
                      "ECON 316": ['ECON 101', 'ECON 103'],
                      "ECON 317": ['ECON 101', 'ECON 103'],
                      "ECON 320": ['ECON 101'],
                      "ECON 321": ['ECON 101', 'ECON 103'],
                      "ECON 332": ['ECON 101'],
                      "ECON 340": ['ECON 101', 'ECON 103'],
                      "ECON 342": ['ECON 101', 'ECON 103'],
                      "ECON 343": ['ECON 101'],
                      "ECON 360": ['ECON 101'],
                      "ECON 381": ['ECON 101'],
                      "ECON 385": ['ECON 101'],
                      "ECON 393": ['ECON 101'],
                      "ECON 415": ['ECON 101', 'ECON 103', 'ECON 306']}

    # blank graph initialized
    g = nx.DiGraph()
    counter = 0
    # loop through each dict key
    for node in adjacency_dict.keys():
        g.add_node(node)

        # loop through each adjacent node
        for adjacent_node in adjacency_dict[node]:
            counter += 1
            # add the edge between the node and the adjacent node
            g.add_edge(adjacent_node, node, weight=counter % 7)



```

**Visualization**:

![Image goes here](ECON_graph.png) 

**Solution code:**

```# the source and destination must be formatted as 'ECON ###' with an existing course #
def find_path(source: str, destination: str, g: nx.DiGraph):
    if nx.has_path(g, source=source, target=destination):
        solution = nx.shortest_path(g, source=source, target=destination, weight='weight')
        return solution, "weight = " + str(nx.path_weight(g, solution, weight='weight'))
    else:
        return "No Path"
```

**Output**

```
(['ECON 101', 'ECON 251', 'ECON 490'], 'weight = 4')
```

**Interpretation of Results**:
	the shortest_path function in the nx library uses Dijkstra's algorithm by default to find the shortest path from one node to another node.

