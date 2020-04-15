import numpy as np
import sys
import pickle as pkl
import networkx as nx
import scipy.sparse as sp


def parse_index_file(filename):
    index = []
    for line in open(filename):
        index.append(int(line.strip()))
    return index


# load the data: x, tx, allx, graph


objects = []
with open("adj.pkl", 'rb+') as f:
    x = pkl.load(f, encoding='latin1')
    print(x)
    print(x.shape)
    print(type(x))


