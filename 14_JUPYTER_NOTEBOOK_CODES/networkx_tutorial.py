import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
nx.draw(G,with_labels=True)
plt.show()

# G.add_nodes_from([1,2,3,4,5,6])
# nx.draw(G,with_labels=True)
# plt.show()

# G.add_nodes_from([
#     (4,{"color":"red"}),
#     (5,{"color":"green"}),
# ])
# nx.draw(G,with_labels=True)
# plt.show()

# H = nx.path_graph(10)
# G.add_nodes_from(H)
# nx.draw(G,with_labels=True)
# plt.show()

# G.add_edge(1,2)
# e = (2,3)
# G.add_edge(*e)
# nx.draw(G,with_labels=True)
# plt.show()

# H = nx.path_graph(10)
# G.add_nodes_from(H)
# G.add_edges_from(H.edges)
# nx.draw(G,with_labels=True)
# plt.show()

# G.add_edges_from([(1,5),(2,5),(1,3),(3,2),(1,4),(4,2),(3,4),(4,5),(5,6),(1,6)])
# nx.draw(G,with_labels=True)
# plt.show()

# G.clear()
# nx.draw(G,with_labels=True)
# plt.show()

# G.add_edges_from([(1,5),(2,5),(1,3),(3,2),(1,4),(4,2),(3,4),(4,5),(5,6),(1,6)])
# nx.draw(G,with_labels=True)
# plt.show()
# print(G.number_of_nodes())
# print(G.number_of_edges())
# print(list(G.nodes))
# print(list(G.edges))
# print(list(G.adj[1])) #return neighbours of 1
# print(G.degree[1]) # return how many node connected with 1
# print(G.degree([1,2])) 
# print(G.edges([6]))

# G.add_edges_from([(1,5),(2,5),(1,3),(3,2),(1,4),(4,2),(3,4),(4,5),(5,6),(1,6)])
# G.remove_node(2)
# nx.draw(G,with_labels=True)
# plt.show()

# G.add_nodes_from("Hitesh")
# G.add_edges_from([(1,"e"),(2,"t"),(1,"h")])
# nx.draw(G,with_labels=True)
# plt.show()

# G.add_nodes_from("Hitesh")
# G.add_edges_from([(1,"e"),(2,"t"),(1,"h")])
# G.remove_nodes_from("Hitesh")
# nx.draw(G,with_labels=True)
# plt.show()

# G.add_nodes_from("Hitesh")
# G.add_edges_from([(1,"e"),(2,"t"),(1,"h")])
# G.remove_edge(1,"e")
# nx.draw(G,with_labels=True)
# plt.show()

# G.add_nodes_from("Hitesh")
# G.add_edges_from([(1,"e"),(2,"t"),(1,"h")])
# G.remove_edges_from([(1,"e"),(2,"t"),(1,"h")])
# nx.draw(G,with_labels=True)
# plt.show()
# plt.savefig("path.png")

# G = nx.complete_graph(5)
# nx.draw(G,with_labels=True)
# plt.show()

# G = nx.complete_bipartite_graph(3,5)
# nx.draw(G,with_labels=True)
# plt.show()

# G = nx.barbell_graph(10,10)
# nx.draw(G,with_labels=True)
# plt.show()

# G = nx.lollipop_graph(10,20)
# nx.draw(G,with_labels=True)
# plt.show()

# G = nx.balanced_tree(2,5)
# nx.draw(G,with_labels=True)
# plt.show()

# G = nx.barabasi_albert_graph(100,5)
# nx.draw(G,with_labels=True)
# plt.show()

# G = nx.watts_strogatz_graph(30,3,0.1)
# nx.draw(G,with_labels=True)
# plt.show()

# G = nx.erdos_renyi_graph(100,0.15)
# nx.draw(G,with_labels=True)
# plt.show()