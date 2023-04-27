#Breadth First Algorithm

import networkx as nx
import matplotlib.pyplot as plt

#Create empty networkx graph 
G = nx.Graph() 

#Add vertices of the graph
G.add_node("Castle") 
G.add_node("Village")
G.add_node("TownSquare") 
G.add_node("Market") 
G.add_node("Abbey") 
G.add_node("Monastery")
G.add_node("Cathedral") 
G.add_node("Church") 
G.add_node("Manor") 
G.add_node("Farmstead") 
G.add_node("Mill") 
G.add_node("Tavern") 
G.add_node("Blacksmith") 
G.add_node("Armory") 
G.add_node("Courtyard") 
G.add_node("GreatHall") 
G.add_node("Dungeon") 
G.add_node("Keep") 
G.add_node("WatchTower") 
G.add_node("MagicForest") 

#Add edges
G.add_edge("Castle", "Village")
G.add_edge("TownSquare", "Village")
G.add_edge("Castle", "TownSquare")
G.add_edge("Abbey", "Market")
G.add_edge("TownSquare", "Abbey")
G.add_edge("Castle", "Monastary")
G.add_edge("TradingPost", "FarmersMarket")
G.add_edge("Church", "Monastery")
G.add_edge("Courtyard", "Church")
G.add_edge("Church", "Cathedral")
G.add_edge("Courtyard", "Manor")
G.add_edge("Farmstead", "Mill")
G.add_edge("Mill", "Manor")
G.add_edge("Courtyard", "Tavern")
G.add_edge("Armory", "Blacksmith")
G.add_edge("GreatHall", "Blacksmith")
G.add_edge("Courtyard", "Armory")
G.add_edge("GreatHall", "Courtyard")
G.add_edge("Keep", "Dungeon")
G.add_edge("MagicForest", "WatchTower")
G.add_edge("Dungeon", "MagicForest")

#Draw graph
nx.draw(G,node_color = "blue", with_labels=True, node_size= 300 )
plt.show()

print(nx.number_connected_components(G))