# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* First member (email)
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
```

# First Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

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

```solution = nx.shortest_path(g, source='ECON 101', target='ECON 490', weight='weight')
```

**Output**

```print(solution)
```

**Interpretation of Results**:

