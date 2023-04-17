import networkx as nx
import matplotlib.pyplot as plt

'''
1. An informal description of the problem, written for intelligent non-Computer Scientists
    In a drastic turn of funding and enrollment, the University of Delaware has approved building a new computer science 
    lab in a number of buildings around campus, with each lab designated for a specific subset of the CISC-coded courses. 
    Unfortunately, due to outdated technology (or perhaps at the request of Dr. Roosen and Dr. Silber) each of these labs
    must be networked directly to the Central UD CISC Server (this defintely exists) at Smith Hall. The problem is to 
    determine the minimum cost for connecting all of the new Labs to the central server and map out this solution. On 
    the map, each line indicates how much it would cost to dig a tunnel to lay the networking cable required to connect 
    each building, or add cable to existing tunnels. (Note: it costs A LOT to dig through the middle of the Green). UD 
    already had to do that once a few years ago, we aren't ruining any more senior pictures!). A cost of 1 on the map 
    translates to $10,000. The map is attatched below.
2. A formal description of the problem, written for other Computer Scientists
    Provided is a graph that contains 20 vertices and 40 edges, representing UD buildings (containing new CISC Labs) and 
    costs of connecting these labs together. The problem is to construct a Minimum Spanning Tree that minimizes the total
    amount of edge weight on the graph using Prim's Algorithm. Following this, calculate the total cost for the project 
    in dollars, where an edge weight of 1 represents $10,000.
3. Which of the four main graph problems you are solving (DFS, BFS, SSSP/APSP, MST)
    MST
4. A visualization of the graph for the problem
    initial-graph.svg
5. The syntax-highlighted code used to load the data into `networkx` and to call the appropriate graph algorithm function
    The below Python code
6. The preformatted output of the graph algorithm function
    ('CISC108', 'CISC181', {'weight': 2})
    ('CISC108', 'CentralUDServer', {'weight': 8})
    ('CISC181', 'CISC220', {'weight': 3})
    ('CISC260', 'CISC360', {'weight': 6})
    ('CISC260', 'CISC361', {'weight': 1})
    ('CISC275', 'CISC355', {'weight': 2})
    ('CISC275', 'CISC498', {'weight': 2})
    ('CISC303', 'CISC260', {'weight': 2})
    ('CISC303', 'CISC275', {'weight': 1})
    ('CISC303', 'CISC304', {'weight': 1})
    ('CISC304', 'CISC483', {'weight': 3})
    ('CISC320', 'CISC484', {'weight': 4})
    ('CISC355', 'CISC108', {'weight': 4})
    ('CISC355', 'CISC499', {'weight': 3})
    ('CISC437', 'CISC320', {'weight': 9})
    ('CISC481', 'CISC437', {'weight': 2})
    ('CISC498', 'CISC372', {'weight': 2})
    ('CentralUDServer', 'CISC210', {'weight': 2})
    ('CentralUDServer', 'CISC481', {'weight': 2})
    Total weight is: 59
    Total cost is: 590000
7. An interpretation of the results that meaningfully answer the question
    A minimum spanning tree that links all of the newly created CISC Labs
    and the main server contains the following nodes:
    ('CISC108', 'CISC181')
    ('CISC108', 'CentralUDServer')
    ('CISC181', 'CISC220')
    ('CISC260', 'CISC360')
    ('CISC260', 'CISC361')
    ('CISC275', 'CISC355')
    ('CISC275', 'CISC498')
    ('CISC303', 'CISC260')
    ('CISC303', 'CISC275')
    ('CISC303', 'CISC304')
    ('CISC304', 'CISC483')
    ('CISC320', 'CISC484')
    ('CISC355', 'CISC108')
    ('CISC355', 'CISC499')
    ('CISC437', 'CISC320')
    ('CISC481', 'CISC437')
    ('CISC498', 'CISC372')
    ('CentralUDServer', 'CISC210')
    ('CentralUDServer', 'CISC481')
    An image of the final Minimum Spanning Tree is attatched below,
    with a total weight of 59, which translates to a total cost for the project
    of $590,000.

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
sum = 0
for edge in sorted_edge_list:
    sum += edge[2]['weight']
print("Total weight is: " + str(sum))
print("Total cost is: " + str(sum*10000))
formatted_output_to_graphviz = [(str(edge[0]) + " -- " + str(edge[1]) + " [label=\"" + str(edge[2]['weight']) + "\"];") for edge in sorted_edge_list]
with open(r'mst-edge-list', 'w') as file:
    for line in formatted_output_to_graphviz:
        file.write("%s\n" % line)