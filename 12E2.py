import matplotlib.pyplot as plt
import networkx as nx
import random

G = nx.Graph()
vlist = list(range(1,random.randint(6,10)))
for v in vlist:
    G.add_node(v)
for v in vlist:
    for w in range(v+1, len(vlist)):
        if random.choice([True, False]):
            G.add_edge(v,w)
nx.draw(G)
plt.show()
