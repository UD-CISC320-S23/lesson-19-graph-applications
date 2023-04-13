import networkx as nx
import matplotlib.pyplot as plt

adjacency_dict = {"MATH 010" : [],
"MATH 114" : ['MATH 010'],
"MATH 115" : ['MATH 010'],
"MATH 221" : ['MATH 115', 'MATH 117'],
"MATH 222" : ['MATH 221', 'MATH 241'],
"MATH 230" : ['MATH 221'],
"MATH 205" : ['MATH 210', 'MATH 230'],
"MATH 349" : ['MATH 230', 'MATH 242'],
"MATH 302" : ['MATH 242', 'MATH 349', 'MATH 351'],
"MATH 420" : ['MATH 302', 'MATH 349', 'MATH 350'],
"MATH 419" : ['MATH 219', 'MATH 243', 'MATH 349', 'MATH 350'],
"MATH 420" : ['MATH 302', 'MATH 349', 'MATH 350'],
"MATH 426" : ['MATH 305', 'MATH 351', 'MATH 349'],
"MATH 428" : ['MATH 426', 'MATH 353'],
"MATH 451" : ['MATH 349', 'MATH 245'],
"MATH 308" : ['MATH 221', 'MATH 232', 'MATH 241'],
"MATH 117" : ['MATH 010'],
"MATH 221" : ['MATH 115', 'MATH 117'],
"MATH 222" : ['MATH 221', 'MATH 241'],
"MATH 230" : ['MATH 221'],
"MATH 205" : ['MATH 210', 'MATH 230'],
"MATH 349" : ['MATH 230', 'MATH 242'],
"MATH 302" : ['MATH 242', 'MATH 349', 'MATH 351'],
"MATH 420" : ['MATH 302', 'MATH 349', 'MATH 350'],
"MATH 419" : ['MATH 219', 'MATH 243', 'MATH 349', 'MATH 350'],
"MATH 420" : ['MATH 302', 'MATH 349', 'MATH 350'],
"MATH 426" : ['MATH 305', 'MATH 351', 'MATH 349'],
"MATH 428" : ['MATH 426', 'MATH 353'],
"MATH 451" : ['MATH 349', 'MATH 245'],
"MATH 308" : ['MATH 221', 'MATH 232', 'MATH 241'],
"MATH 241" : ['MATH 117'],
"MATH 219" : ['MATH 241'],
"MATH 419" : ['MATH 219', 'MATH 243', 'MATH 349', 'MATH 350'],
"MATH 222" : ['MATH 221', 'MATH 241'],
"MATH 242" : ['MATH 241', 'MATH 232'],
"MATH 243" : ['MATH 242'],
"MATH 379" : ['MATH 243'],
"MATH 380" : ['MATH 379'],
"MATH 382" : ['MATH 380'],
"MATH 419" : ['MATH 219', 'MATH 243', 'MATH 349', 'MATH 350'],
"MATH 245" : ['MATH 210', 'MATH 242'],
"MATH 401" : ['MATH 245'],
"MATH 451" : ['MATH 349', 'MATH 245'],
"MATH 302" : ['MATH 242', 'MATH 349', 'MATH 351'],
"MATH 420" : ['MATH 302', 'MATH 349', 'MATH 350'],
"MATH 305" : ['MATH 242'],
"MATH 426" : ['MATH 305', 'MATH 351', 'MATH 349'],
"MATH 428" : ['MATH 426', 'MATH 353'],
"MATH 349" : ['MATH 230', 'MATH 242'],
"MATH 302" : ['MATH 242', 'MATH 349', 'MATH 351'],
"MATH 420" : ['MATH 302', 'MATH 349', 'MATH 350'],
"MATH 419" : ['MATH 219', 'MATH 243', 'MATH 349', 'MATH 350'],
"MATH 420" : ['MATH 302', 'MATH 349', 'MATH 350'],
"MATH 426" : ['MATH 305', 'MATH 351', 'MATH 349'],
"MATH 428" : ['MATH 426', 'MATH 353'],
"MATH 451" : ['MATH 349', 'MATH 245'],
"MATH 308" : ['MATH 221', 'MATH 232', 'MATH 241'],
"MATH 231" : ['MATH 010'],
"MATH 232" : ['MATH 231'],
"MATH 242" : ['MATH 241', 'MATH 232'],
"MATH 243" : ['MATH 242'],
"MATH 379" : ['MATH 243'],
"MATH 380" : ['MATH 379'],
"MATH 382" : ['MATH 380'],
"MATH 419" : ['MATH 219', 'MATH 243', 'MATH 349', 'MATH 350'],
"MATH 245" : ['MATH 210', 'MATH 242'],
"MATH 401" : ['MATH 245'],
"MATH 451" : ['MATH 349', 'MATH 245'],
"MATH 302" : ['MATH 242', 'MATH 349', 'MATH 351'],
"MATH 420" : ['MATH 302', 'MATH 349', 'MATH 350'],
"MATH 305" : ['MATH 242'],
"MATH 426" : ['MATH 305', 'MATH 351', 'MATH 349'],
"MATH 428" : ['MATH 426', 'MATH 353'],
"MATH 349" : ['MATH 230', 'MATH 242'],
"MATH 302" : ['MATH 242', 'MATH 349', 'MATH 351'],
"MATH 420" : ['MATH 302', 'MATH 349', 'MATH 350'],
"MATH 419" : ['MATH 219', 'MATH 243', 'MATH 349', 'MATH 350'],
"MATH 420" : ['MATH 302', 'MATH 349', 'MATH 350'],
"MATH 426" : ['MATH 305', 'MATH 351', 'MATH 349'],
"MATH 428" : ['MATH 426', 'MATH 353'],
"MATH 451" : ['MATH 349', 'MATH 245'],
"MATH 308" : ['MATH 221', 'MATH 232', 'MATH 241'] }

# create an empty graph
G = nx.Graph()

# loop through each key in the dictionary
for node in adjacency_dict.keys():

    # add the node to the graph
    G.add_node(node)

    # loop through each of its adjacent nodes
    for adjacent_node in adjacency_dict[node]:

        # add the edge between the node and the adjacent node
        G.add_edge(node, adjacent_node)
        
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
plt.show()