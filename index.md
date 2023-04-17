# Title of Your Project

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* First member (email)
* ebrignac@udel.edu 
* jfmarks@udel.edu
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




# Using DFS to find the lowest CISC course number in the graph

**Informal Description**:
Bob wants to find the easiest computer science course. Foolishly, Bob thinks that the easiest course is the one with the lowest Course ID.

> **Formal Description**:
>  * Input: 'CISC 499', and the CISC course graph
>  * Output: CISC 108

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]
    DFS

**Setup code**:

```
   adjacency_dict = {
'CISC 108': [],
'CISC 181': ['CISC 108'],
'CISC 250': ['CISC 181'],
'CISC 275': ['CISC 181', 'CISC 220'],
'CISC 415': ['CISC 275'],
'CISC 474': ['CISC 275'], 
'CISC 475': ['CISC 275', 'CISC 361'],
'CISC 482': ['CISC 275'], 
'CISC 498': ['CISC 275'],
'CISC 499': ['CISC 320', 'CISC 498'],
'CISC 204': ['CISC 108'], 
'CISC 210': ['CISC 108'],
'CISC 220': ['CISC 210'],
'CISC 303': ['CISC 220'],
'CISC 401': ['CISC 303'], 
'CISC 471': ['CISC 260', 'CISC 303'],
'CISC 304': ['CISC 220'],
'CISC 404': ['CISC 304'],
'CISC 414': ['CISC 304'],
'CISC 481': ['CISC 220', 'CISC 304'], 
'CISC 320': ['CISC 220'], 
'CISC 358': ['CISC 220'],
'CISC 360': ['CISC 220', 'CISC 260'],
'CISC 361': ['CISC 220', 'CISC 260'],
'CISC 469': ['CISC 361'],
'CISC 479': ['CISC 361'],
'CISC 362': ['CISC 220'],
'CISC 372': ['CISC 220', 'CISC 260'],
'CISC 374': ['CISC 220'],
'CISC 436': ['CISC 220'],
'CISC 437': ['CISC 220'],
'CISC 440': ['CISC 220'],
'CISC 442': ['CISC 220'],
'CISC 483': ['CISC 220'],
'CISC 484': ['CISC 220'],
'CISC 486': ['CISC 220'],
'CISC 488': ['CISC 220'], 
'CISC 260': ['CISC 210'],
'CISC 450': ['CISC 260'],
'CISC 453': ['CISC 450'],
'CISC 459': ['CISC 450'],
'CISC 464': ['CISC 450'],
'CISC 357': ['CISC 108']}

import networkx as nx

G = nx.DiGraph(adjacency_dict)


```

**Visualization**:

![Image goes here](CISC_graph.png) 

**Solution code:**

```# the source and destination must be formatted as 'ECON ###' with an existing course #
def find_easiest_course(course):
    # Find the easiest course in the graph
    # The easiest course == the course with the lowest course number


    # Perform depth-first search to search all nodes of depth 2
    dfs_edges = nx.dfs_edges(G, course)

    # Print the edges visited during the depth-first search
    
    m = int(course[-3:])
    for edge in dfs_edges:
        print(edge)
        if int(edge[0][-3:]) < m:
            m = int(edge[0][-3:])
        if int(edge[1][-3:]) < m:
            m = int(edge[1][-3:])
    return 'CISC ' + str(m)
```

**Output**

```
CISC 108
```

**Interpretation of Results**:
	The Depth first search algorith scans over all of the nodes in the graph so we can use
    it to find the node with the smallest course number. 








