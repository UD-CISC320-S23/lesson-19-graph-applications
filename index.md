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

# Second Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: [MST(Prims)]


**Setup code**:

```import matplotlib.pyplot as plt import networkx as nx
```

**Visualization**:

![Prims Graph](https://i.ibb.co/FnvVfKj/prims.png)

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

    nx.draw_networkx(G, pos, node_color='#0091e6', node_size=300,
                     font_size=7,
                     font_color='white',
                     edge_color='black',
                     font_weight='bold',
                     width=3,
                     with_labels=True)
    

    


    nx.draw_networkx_edges(MST, pos, edge_color='#0091e6', style='dashed', width=3)

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

    
main()

**Output**

```
```

**Interpretation of Results**:

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