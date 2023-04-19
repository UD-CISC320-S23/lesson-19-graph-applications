# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* First member aoster@udel.edu
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
DFS on FriendShip Graph to Determine Number of Groups (Connected Components) In 
Ancient Kingdom.
**Informal Description**: 
Takes a graph and determines the number of connected components that exist in that graph
> **Formal Description**:
>  * Input: G(V, E): Graph of Vertices and Edges
>  * Output: Int: Number of Connected Components

**Graph Problem/Algorithm**: [DFS]
DFS

**Setup code**:

```python
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node("K") #King
G.add_node("Q") #Queen
G.add_node("Kn") #Knight
G.add_node("Peasants")
G.add_node("G") #Gaurds
G.add_node("F") #Farmer
G.add_node("W") #Witch
G.add_node("Ma") #Magician
G.add_node("M") #Mathematician
G.add_node("A") #Astronomer
G.add_node("S") #Sailor
G.add_node("Mo") #MonK
G.add_node("mer") #Merchant
G.add_node("B") #Botanist
G.add_node("Dr") #Doctor
G.add_node("Prank") #Prankster
G.add_node("d") #drunkard
G.add_node("Ph") #Philosopher
G.add_edge("Ph", "M", )
G.add_edge("M","A")
G.add_edge("W", "Ma")
G.add_edge("Dr", "M")
G.add_edge("Dr", "A")
G.add_edge("K", "Q")
G.add_edge("K", "Kn")
G.add_edge("K", "G")
G.add_edge("Q", "KN")
G.add_edge("Q", "G")
G.add_edge("mer", "F")
G.add_edge("mer", "S")
G.add_edge("F", "S")
G.add_edge("Ma", "W")
G.add_edge("W", "d")
G.add_edge("B", "mer")
G.add_edge("Mo", "M")
G.add_edge("Mo", "Dr")
G.add_edge("Ph", "Mo")
G.add_edge("Prank", "Ma")

nx.draw(G,node_color = "red",with_labels=True, node_size= 300 )
```

**Visualization**:

![Image goes here](FriendshipGraph.png)

**Solution code:**

```python
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node("K") #King
G.add_node("Q") #Queen
G.add_node("Kn") #Knight
G.add_node("Peasants")
G.add_node("G") #Gaurds
G.add_node("F") #Farmer
G.add_node("W") #Witch
G.add_node("Ma") #Magician
G.add_node("M") #Mathematician
G.add_node("A") #Astronomer
G.add_node("S") #Sailor
G.add_node("Mo") #MonK
G.add_node("mer") #Merchant
G.add_node("B") #Botanist
G.add_node("Dr") #Doctor
G.add_node("Prank") #Prankster
G.add_node("d") #drunkard
G.add_node("Ph") #Philosopher
G.add_edge("Ph", "M", )
G.add_edge("M","A")
G.add_edge("W", "Ma")
G.add_edge("Dr", "M")
G.add_edge("Dr", "A")
G.add_edge("K", "Q")
G.add_edge("K", "Kn")
G.add_edge("K", "G")
G.add_edge("Q", "KN")
G.add_edge("Q", "G")
G.add_edge("mer", "F")
G.add_edge("mer", "S")
G.add_edge("F", "S")
G.add_edge("Ma", "W")
G.add_edge("W", "d")
G.add_edge("B", "mer")
G.add_edge("Mo", "M")
G.add_edge("Mo", "Dr")
G.add_edge("Ph", "Mo")
G.add_edge("Prank", "Ma")

nx.draw(G,node_color = "red",with_labels=True, node_size= 300 )
print(nx.number_connected_components(G))

```

**Output**

```
5
```

**Interpretation of Results**:
This means that there are 5 different connected graphs. This means that there are 5 different social groups and people are disconnected from one another. It is interesting to see how is more connected to each other than other types of people.
