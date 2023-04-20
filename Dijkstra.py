#a mathematician is trying to find the shortest path from the  inside a city to the kings castle
#the king is very nervous the witch may try to poison the towns water supply, and 
#A notorious witch lives in the town of ____, and she gives King ___ the creeps. He is nervous the Witch may poison the water supply
#so he asked his most trustworthy Mathematician Chatus Gptus to determine which roads would provide the quickest travel between the 
#witches hut and the castle, so, should anything fishy occur, his knights could swiftly deliever judgement to the witch. 
#
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node("Castle") 
G.add_node("WitchHut") #Queen
G.add_node("FlowerShop") #Knight
G.add_node("Piazza")
G.add_node("FarmersMarket") #Gaurds
G.add_node("MysteryShack") #Farmer
G.add_node("Well") #Witch
G.add_node("Guardpost") #Magician
G.add_node("Observatory") #Mathematician
G.add_node("Dock") #Astronomer
G.add_node("Monastary") #Sailor
G.add_node("TradingPost") #MonK
G.add_node("Hospital") #Merchant
G.add_node("Saloon") #Botanist
G.add_node("Backrooms") #Doctor
G.add_node("School") #Prankster
G.add_node("ManorHouse") #drunkard
G.add_node("Cottage") #Philosopher
G.add_node("Stables") 
G.add_edge("Castle", "Guardpost", weight=1)
G.add_edge("Guardpost", "Stables", weight=2)
G.add_edge("Stables", "Saloon", weight=6)
G.add_edge("Hospital", "Stables", weight=4)
G.add_edge("Saloon", "Dock", weight=7)
G.add_edge("Observatory", "Monastary", weight=2)
G.add_edge("TradingPost", "FarmersMarket", weight=1)
G.add_edge("WitchHut", "MysteryShack", weight=3)
G.add_edge("MysteryShack", "Well", weight=15)
G.add_edge("School", "Well", weight=5)
G.add_edge("Well", "FarmersMarket", weight=3)
G.add_edge("FlowerShop", "Well", weight=3)
G.add_edge("Cottage", "ManorHouse", weight=11)
G.add_edge("Piazza", "Well", weight=1)
G.add_edge("FlowerShop", "Piazza", weight=4)
G.add_edge("School", "Piazza", weight=2)
G.add_edge("Monastary", "Piazza", weight=3)
G.add_edge("Hospital", "Saloon", weight=3)
G.add_edge("Hospital", "School", weight=7)
G.add_edge("Cottage", "FarmersMarket", weight=3)
G.add_edge("ManorHouse", "FarmersMarket", weight=3)

nx.draw(G,node_color = "green",with_labels=True, node_size= 300 )
plt.show()