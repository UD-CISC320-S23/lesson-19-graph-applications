import networkx as nx
import matplotlib.pyplot as plt

'''
1. An informal description of the problem, written for intelligent non-Computer Scientists
    In a drastic turn of funding and enrollment, the uninversity has approved building a new computer science lab in a 
    number of buildings around campus, with each lab designated for a specific subset of the CISC-coded courses. 
    Unfortunately, due to outdated technology (or perhaps at the request of Dr. Roosen and Dr. Silber) each of these labs
    must be networked directly to the Central UD CISC Server (this defintely exists) at Smith Hall. Our problem is to 
    determine the minimum cost for connecting all of the new Labs to the central server by constructing a Minimum 
    Spanning Tree of campus between these Labs.

2. A formal description of the problem, written for other Computer Scientists
    We hav
3. Which of the four main graph problems you are solving (DFS, BFS, SSSP/APSP, MST)
    MST
4. A visualization of the graph for the problem
    graphviz.svg
5. The syntax-highlighted code used to load the data into `networkx` and to call the appropriate graph algorithm function
    The below Python code
6. The preformatted output of the graph algorithm function
7. An interpretation of the results that meaningfully answer the question
'''
lab_map = nx.Graph()
edges = []
with open('edge-list.txt') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        nodes = line.split(' ')
        node0 = nodes[0]
        node1 = nodes[2]
        weight = nodes[3].split("\"")[1]
        edges.append((node0, node1, int(weight)))

print(edges)
lab_map.add_weighted_edges_from(edges)
print(lab_map)

mst = nx.tree.minimum_spanning_edges(lab_map, algorithm='prim', data=False)
edgelist = list(mst)
x = sorted(edgelist)
print(x)
print(len(x))