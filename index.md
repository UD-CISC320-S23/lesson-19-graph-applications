# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Paul Kearney (paulke@udel.edu)
* Second member (email)
* Third member (email)
* Fourth member (email)

Description of project

We are planning a trip for this summer. we wish to fly somewhere far away/exotic and pick a great plan for visiting
all of the tourist destinations wherever we choose to visit has to offer on a budget. aswell as packlight to avoid
any baggage fees with heavy luggage 

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# First Problem Title
Turist destinations
**Informal Description**: 
After Landing in LA, we want to see as much as possible, but we are in a time crunch. well have to see how long of a 
dive is to be expected between destinations and pick the best path for seeing the most in the shortest amount of time
before we have to drive back to an airport.
> **Formal Description**:
>  * Input: An undirected graph of tourist destinations. 
>  * Output: minimum spanning tree of tourist destinations

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]


**Setup code**:

```python
import networkx as nx
edges = []
with open("tourist_destinations.txt") as data_file:
    lines: list[str]
    lines = data_file.readlines()
destinations = nx.Graph()
for line in lines:
    nx.add_node(line)
    
with open("tourist_edges.txt") as data_file:
    lines: list[str]
    lines = data_file.readlines()
for line in lines:
    edges.append(line.split(","))
for line in lines:
    nx.add_edge(edges[0], edges[1],edges[2])
    

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

