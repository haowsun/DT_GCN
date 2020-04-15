import networkx as nx
import pickle as pkl
import numpy as np

a = np.loadtxt('drugProtein.txt')
m, n = a.shape[0], a.shape[1]  #
print(m, n)
dim = m + n  # 邻接矩阵的维度

print(a)
print(a.shape)
G = nx.Graph()
H = nx.path_graph(dim)
G.add_nodes_from(H)
num = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == 1:
            G.add_edge(i, m + j)

adj = nx.adjacency_matrix(G)
with open('DT.adj.pkl', 'wb') as f:
    pkl.dump(adj, f)

print(adj)
print(adj.shape)
print(type(adj))
