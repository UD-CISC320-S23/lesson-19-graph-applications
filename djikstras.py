import networkx as nx
import matplotlib.pyplot as plt
graph = {"PHL":{"LAX": {'weight': 8}, "CLT": {'weight': 2}, "PHX":{'weight': 6},
                "ORD": {'weight': 3},"ATL":{'weight':2},"BOS":{"weight":1}},
          "CLT": {"MIA":{"weight":2},"STL":{"weight":2},"DFW":{"weight":4},
                  "MEM":{"weight":1},"DEN":{"weight":4}},
          "PHX": {"LAX": {'weight': 2},"DEN":{"weight":3},"STL":{"weight":4}},
          "ORD": {"LAX": {"weight": 5},"DFW":{"weight":6}, "ATL":{"weight":5}},
          "IAD": {"BOS":{"weight":2},"ATL":{"weight":3}},
          "SEA": {"LAS": {'weight': 3}, "SFO":{'weight':2}, "SLC":{"weight":3},
                  "ORD":{'weight':5}},
          "LAS": {"LAX":{"weight":1}, "MIA":{"weight":9},"MEM":{"weight":4}},
          "SFO":{"LAX":{"weight":1},"DEN":{'weight':2},"STL":{"weight":4},},
          "DFW":{"DEN":{"weight":2},"MIA":{"weight":4},"DTW":{"weight":5},
                 "CLE":{"weight":4}},
          "MIA":{"ATL":{"weight":2},"IAD":{"weight":4},"BOS":{"weight":7}},
          "STL":{"MEM":{"weight":2},"SLC":{"weight":3}, "DTW":{"weight":1},
                 "CLE":{"weight":1}},
          "BOS":{"LAX":{"weight":10},"CLE":{"weight":5},"CLE":{"weight":2}},
          "HNL": {"LAX":{"weight":13},"SFO":{"weight":13}}
          }
G = nx.from_dict_of_dicts(graph)

pos = nx.shell_layout(G)
labels = nx.get_edge_attributes(G,'weight')
plt.figure(1,figsize=(12,12)) 
nx.draw_networkx(G,pos, node_size=100, font_size=16)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("graph_for_djikstras_shell.png")

djikstra = nx.dijkstra_path(G,"ATL","LAS", weight='weight')
print(djikstra)

