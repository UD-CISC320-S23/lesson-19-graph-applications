import networkx as nx

# digraph Udel {
    
#    Frazer_field -> Lil_bob [dir=none] d
#    Lil_bob -> {Taylor Old_College Brown_hall} [dir=none] d
#    Willard_hall -> {McDowell_hall Old_College Trabant} [dir=none] d
#    Taylor -> Old_College [dir=none] d
#    Brown_hall -> {Harter Syperd Sharp_hall} [dir=none] d
#    Harter -> {Syperd Sharp_hall} [dir=none] d
#    Syperd -> {Sharp_hall} [dir=none] d
#    Trabant -> {Kirkbride Sharp_lab Ewing} [dir=none] d
#    Kirkbride -> {Ewing Purnell Smith} [dir=none] d
#    Ewing -> {Purnell Smith} [dir=none] d
#    Purnell -> {Smith} [dir=none] d
#    Sharp_lab -> {Wolf Gore} [dir=none] d
#    Gore -> {Mitchell Memorial Brown_lab Smith} [dir=none] d
#    Brown_lab -> {Colburn ICE} [dir=none] d
#    Morris -> {Memorial Allison Perkins} [dir=none] d
#    Perkins -> {Redding Russel Harrington} [dir=none] d
#    Harrington -> {Russel Redding} [dir=none] d
#    Redding -> Russel [dir=none] d
#    ICE -> {Penny Colburn Spencer_lab} [dir=none] d
#    Spencer_lab -> Colburn [dir=none] d
#    Allison -> {Perkins Penny} [dir=none] d
       
#    }


g = nx.Graph()
g.add_edge("Frazer Field", "Lil Bob", weight = 1)
g.add_edges_from([("Lil Bob", "Taylor"), ("Lil Bob", "Old College"), ("Lil Bob", "Brown Hall")], weight = 3)
g.add_edges_from([("Willard Hall", "McDowell Hall"), ("Willard Hall", "Old College"), ("Willard Hall", "Trabant")], weight = 2)
g.add_edge("Taylor", "Old College", weight = 1)
g.add_edges_from([("Brown Hall", "Harter"), ("Brown Hall", "Sypherd"), ("Brown Hall", "Sharp Hall")], weight = 1)
g.add_edges_from([("Harter", "Sypherd"), ("Harter", "Sharp Hall")], weight = 1)
g.add_edges_from([("Trabant", "Kirkbride"), ("Trabant", "Sharp Lab"), ("Trabant", "Ewing")], weight = 3)
g.add_edges_from([("Kirkbride", "Ewing"), ("Kirkbride", "Purnell"), ("Kirkbride", "Smith")], weight = 1)
g.add_edges_from([("Ewing", "Purnell"), ("Ewing", "Smith")], weight = 1)
g.add_edge("Purnell", "Smith", weight = 1)
g.add_edges_from([("Sharp Lab", "Wolf"), ("Sharp Lab", "Gore")], weight = 2)
g.add_edges_from([("Gore", "Mitchell"), ("Gore", "Memorial"), ("Gore", "Brown Lab"), ("Gore", "Smith")], weight = 2)
g.add_edges_from([("Brown Lab", "Colburn"), ("Brown Lab", "ICE")], weight = 4)
g.add_edges_from([("Morris", "Memorial"), ("Morris", "Allison"), ("Morris", "Perkins")], weight = 3)
g.add_edges_from([("Perkins", "Redding"), ("Perkins", "Russel"), ("Perkins", "Harrington")], weight = 3)
g.add_edges_from([("Harrington", "Russel"), ("Harrington", "Redding")], weight = 2)
g.add_edge("Redding", "Russel", weight = 2)
g.add_edges_from([("ICE", "Penny"), ("ICE", "Colburn"), ("ICE", "Spencer Lab")], weight = 3)
g.add_edge("Spencer Lab", "Colburn", weight = 2)
g.add_edges_from([("Allison", "Perkins"), ("Allison", "Penny")], weight = 4)

# test, morris-> allison-> penny
print(nx.shortest_path(g, "Morris", "Penny", weight = "weight"))