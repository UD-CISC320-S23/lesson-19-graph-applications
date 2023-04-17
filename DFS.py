# the dictionary containing the adjacency for the graph
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

# Test the function
easy = find_easiest_course('CISC 499')
print(easy)

