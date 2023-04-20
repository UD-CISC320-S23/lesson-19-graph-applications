import networkx as nx
G = nx.MultiGraph()
elistrow = [(1, 2, 1), (2, 3, 1), (3, 4, 3), (4, 5, 3), (5, 6, 2), (6, 7, 1), (7, 8, 1),
            (9, 10, 3), (10, 11, 2), (11, 12, 3), (12, 13, 1), (13, 14, 1),(14, 15, 2), (15, 16, 1),
            (17, 18, 1), (18, 19, 1), (19, 20, 3), (20, 21, 3), (21, 22, 2), (22, 23, 1), (23, 24, 1),
            (25, 26, 3), (26, 27, 2), (27, 28, 3), (28, 29, 1), (29, 30, 1), (30, 31, 2), (31, 32, 1),
            (33, 34, 1), (34, 35, 1), (35, 36, 3), (36, 37, 3), (37, 38, 2), (38, 39, 1), (39, 40, 1),
            (41, 42, 3), (42, 43, 2), (43, 44, 3), (44, 45, 1), (45, 46, 1), (46, 47, 2), (47, 48, 1),
            (49, 50, 1), (50, 51, 1), (51, 52, 3), (52, 53, 3), (53, 54, 2), (54, 55, 1), (55, 56, 1),
            (57, 58, 3), (58, 59, 2), (59, 60, 3), (60, 61, 1), (61, 62, 1), (62, 63, 2), (63, 64, 1)]
elistcol = [(1, 9, 1), (9, 17, 3), (17, 25, 1), (25, 33, 3), (33, 41, 1), (41, 49, 3), (49, 57, 1),
            (2, 10, 1), (10, 18, 2), (18, 26, 1), (26, 34, 2), (34, 42, 1), (42, 50, 2), (50, 58, 1),
            (3, 11, 3), (11, 19, 3), (19, 27, 3), (27, 35, 3), (35, 43, 3), (43, 51, 3), (51, 59, 3),
            (4, 12, 3), (12, 20, 1), (20, 28, 3), (28, 36, 1), (36, 44, 3), (44, 52, 1), (52, 60, 3),
            (5, 13, 2), (13, 21, 1), (21, 29, 2), (29, 37, 1), (37, 45, 2), (45, 53, 1), (53, 61, 2),
            (6, 14, 1), (14, 22, 2), (22, 30, 1), (30, 38, 2), (38, 46, 1), (46, 54, 2), (54, 62, 1),
            (7, 15, 1), (15, 23, 1), (23, 31, 1), (31, 39, 1), (39, 47, 1), (47, 55, 1), (55, 63, 1),
            (8, 16, 2), (16, 24, 1), (24, 32, 2), (32, 40, 1), (40, 48, 2), (48, 56, 1), (56, 64, 2),]
G.add_weighted_edges_from(elistrow)
G.add_weighted_edges_from(elistcol)
if __name__ == "__main__":
    shortest_path = nx.dijkstra_path(G, 1, 64)
    print(shortest_path)
