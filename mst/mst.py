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
    ('CISC108', 'CISC355', {'weight': 4})
    ('CISC181', 'CISC108', {'weight': 2})
    ('CISC210', 'CISC220', {'weight': 8})
    ('CISC220', 'CISC181', {'weight': 3})
    ('CISC260', 'CISC360', {'weight': 6})
    ('CISC260', 'CISC361', {'weight': 1})
    ('CISC275', 'CISC303', {'weight': 1})
    ('CISC275', 'CISC498', {'weight': 2})
    ('CISC303', 'CISC260', {'weight': 2})
    ('CISC303', 'CISC304', {'weight': 1})
    ('CISC304', 'CISC483', {'weight': 3})
    ('CISC320', 'CISC484', {'weight': 4})
    ('CISC355', 'CISC275', {'weight': 2})
    ('CISC355', 'CISC499', {'weight': 3})
    ('CISC437', 'CISC210', {'weight': 2})
    ('CISC437', 'CISC320', {'weight': 9})
    ('CISC437', 'CISC481', {'weight': 2})
    ('CISC481', 'CentralUDServer', {'weight': 2})
    ('CISC498', 'CISC372', {'weight': 2})
7. An interpretation of the results that meaningfully answer the question
    Thus, A minimum spanning tree that links all of the newly created CISC
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

mst = nx.tree.minimum_spanning_edges(lab_map, algorithm='prim', data=True)
edge_list = list(mst)
sorted_edge_list = sorted(edge_list)
[print(edge) for edge in sorted_edge_list] #preformatted output
formatted_output_to_graphviz = [(str(edge[0]) + " -- " + str(edge[1]) + " [label=\"" + str(edge[2]['weight']) + "\"];") for edge in sorted_edge_list]
print(formatted_output_to_graphviz)
with open(r'mst-edge-list', 'w') as file:
    for line in formatted_output_to_graphviz:
        file.write("%s\n" % line)