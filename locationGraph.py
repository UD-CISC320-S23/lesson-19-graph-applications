# digraph Udel {
    
#    Frazer_field -> Lil_bob [dir=none]
#    Lil_bob -> {Taylor Old_College Brown_hall} [dir=none]
#    Willard_hall -> {McDowell_hall Old_College Trabant} [dir=none]
#    Taylor -> Old_College [dir=none]
#    Brown_hall -> {Harter Syperd Sharp_hall} [dir=none]
#    Harter -> {Syperd Sharp_hall} [dir=none]
#    Syperd -> {Sharp_hall} [dir=none]
#    Trabant -> {Kirkbride Sharp_lab Ewing} [dir=none]
#    Kirkbride -> {Ewing Purnell Smith} [dir=none]
#    Ewing -> {Purnell Smith} [dir=none]
#    Purnell -> {Smith} [dir=none]
#    Sharp_lab -> {Wolf Gore} [dir=none]
#    Gore -> {Mitchell Memorial Brown_lab Smith} [dir=none]
#    Brown_lab -> {Colburn ICE} [dir=none]
#    Morris -> {Memorial Allison Perkins} [dir=none]
#    Perkins -> {Redding Russel Harrington} [dir=none]
#    Harrington -> {Russel Redding} [dir=none]
#    Redding -> Russel [dir=none]
#    ICE -> {Penny Colburn Spencer_lab} [dir=none]
#    Spencer_lab -> Colburn [dir=none]
#    Allison -> {Perkins Penny} [dir=none]
       
#    }

import networkx as nx

g = nx.Graph()
g.add_edge("A", "B", weight = 4)
g.add_edge("B", "D", weight = 2)
f = nx.shortest_path(g, "A", "D", weight = "weight")
print(f)