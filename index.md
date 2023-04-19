# Team Dragon

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Nick Lago (nlago@udel.edu)
* Hongbo Wang (frankw@udel.edu)
* Patrick Harris (pdharris@udel.edu)
* John Henry Cooper (jhcoop@udel.edu)

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

**Graph Problem/Algorithm**: [SSSP(Djikstras)]


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

# Minimum Distance Path (Kruskals)

**Informal Description**: Kruskals Algorithm finds the minimum spanning tree of a given weighted undirected graph. In this case, the algorithm finds the flight path with the minimum distance covered in order to still reach every location/airport.

> **Formal Description**:
>  * Input: Flights.csv:  
NY,NJ,4
NY,RI,7
NJ,CT,6
RI,CT,1
CT,PA,10
RI,PA,5
FL,TX,14
FL,OK,8
OK,TX,4
TX,KY,5
KY,MN,4
MN,IL,6
MN,OH,8
IL,OH,1
CT,VA,7
KY,LO,4
LO,AK,3
LO,MS,5
MS,AK,1
NJ,ME,6
NY,NH,3
TX,CO,8
TN,AK,10
NH,TX,45
RI,MS,16
ME,FL,20
OK,MS,5
IL,TN,50
OH,CO,60
AK,PA,55  

>  * Output: Graph with 20 nodes and 19 edges
('RI', 'CT', {'d': 1.0})
('IL', 'OH', {'d': 1.0})
('AK', 'MS', {'d': 1.0})
('NY', 'NH', {'d': 3.0})
('LO', 'AK', {'d': 3.0})
('NY', 'NJ', {'d': 4.0})
('TX', 'OK', {'d': 4.0})
('KY', 'MN', {'d': 4.0})
('KY', 'LO', {'d': 4.0})
('RI', 'PA', {'d': 5.0})
('TX', 'KY', {'d': 5.0})
('NJ', 'CT', {'d': 6.0})
('NJ', 'ME', {'d': 6.0})
('MN', 'IL', {'d': 6.0})
('CT', 'VA', {'d': 7.0})
('FL', 'OK', {'d': 8.0})
('TX', 'CO', {'d': 8.0})
('AK', 'TN', {'d': 10.0})
('RI', 'MS', {'d': 16.0})

**Graph Problem/Algorithm**: [MST (Kruskals)]


**Setup code**:

import matplotlib.pyplot as plt  
import networkx as nx

**Visualization**:

![https://i.ibb.co/FnvVfKj/prims.png](https://i.ibb.co/FnvVfKj/prims.png)  
Minimum spanning tree is shown in blue dashed lines over the edges.

**Solution code:**

```
    def main():
    with open("Flights.csv") as data_file:
        lines = data_file.readlines()
    
    G=nx.Graph()

    for line in lines:
        start, end, weight = line.strip("\n").split(",")
        weight=float(weight)
        G.add_edge(start, end, d=weight)

    MST = nx.minimum_spanning_tree(G, weight="d", algorithm="kruskal")
    
    pos = nx.spring_layout(G)

    nx.draw_networkx(G, 
        pos, 
        node_color='#0091e6', 
        node_size=300,
        font_size=7,
        font_color='white',
        edge_color='black',
        font_weight='bold',
        width=3,
        with_labels=True)

    nx.draw_networkx_edges(MST, 
        pos, 
        edge_color='#0091e6',
        style='dashed', 
        width=3)

    nx.draw_networkx_edge_labels(G, pos, 
        label_pos=0.5, 
        font_size=4, 
        font_color='k', 
        font_family='sans-serif',
        font_weight='bold', 
        horizontalalignment='center', 
        verticalalignment="bottom",
        rotate=True, 
        clip_on=True)
        
    plt.axis('off')
    plt.show()
    print(nx.minimum_spanning_tree(G, weight="d", algorithm="kruskal"))
    
main()
```

**Output**

```
    Graph with 20 nodes and 19 edges
(‘RI’, ‘CT’, {‘d’: 1.0})
(‘IL’, ‘OH’, {‘d’: 1.0})
(‘AK’, ‘MS’, {‘d’: 1.0})
(‘NY’, ‘NH’, {‘d’: 3.0})
(‘LO’, ‘AK’, {‘d’: 3.0})
(‘NY’, ‘NJ’, {‘d’: 4.0})
(‘TX’, ‘OK’, {‘d’: 4.0})
(‘KY’, ‘MN’, {‘d’: 4.0})
(‘KY’, ‘LO’, {‘d’: 4.0})
(‘RI’, ‘PA’, {‘d’: 5.0})
(‘TX’, ‘KY’, {‘d’: 5.0})
(‘NJ’, ‘CT’, {‘d’: 6.0})
(‘NJ’, ‘ME’, {‘d’: 6.0})
(‘MN’, ‘IL’, {‘d’: 6.0})
(‘CT’, ‘VA’, {‘d’: 7.0})
(‘FL’, ‘OK’, {‘d’: 8.0})
(‘TX’, ‘CO’, {‘d’: 8.0})
(‘AK’, ‘TN’, {‘d’: 10.0})
(‘RI’, ‘MS’, {‘d’: 16.0})
```

**Interpretation of Results**: These results tell the traveler the path that connects all states' airports in the least distance covered. This can be useful for anyone who is looking to travel to multiple destinations, and wants to be time efficient in doing so. A minimum spanning tree can also be a helpful visual for airlines when choosing optimal routes to fly.

# Third Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: [DFS]


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

# Fourth Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: [BFS]


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