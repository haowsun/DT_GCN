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


def load_data(dataset):
    # load the data: x, tx, allx, graph
    if dataset == 'DDT':
        print('yes')
        with open('data/DDT.adj.pkl', 'rb') as f:
            adj = pkl.load(f)

        print(adj.shape)
        with open('data/DDT.feature.pkl', 'rb') as f:
            features = pkl.load(f, encoding='latin1')
        features = sp.lil_matrix(features)
        print(features.shape)
        return adj, features
    if dataset == 'DD_combine':
        print('yes')
        with open('data/DD_combine.adj.pkl', 'rb') as f:
            adj = pkl.load(f)

        print(adj.shape)
        with open('data/DD_combine.feature.pkl', 'rb') as f:
            features = pkl.load(f, encoding='latin1')
        features = sp.lil_matrix(features)
        print(features.shape)
        return adj, features
    names = ['x', 'tx', 'allx', 'graph']
    objects = []
    for i in range(len(names)):
        with open("data/ind.{}.{}".format(dataset, names[i]), 'rb') as f:
            if sys.version_info > (3, 0):
                objects.append(pkl.load(f, encoding='latin1'))
            else:
                objects.append(pkl.load(f))
    x, tx, allx, graph = tuple(objects)
    test_idx_reorder = parse_index_file("data/ind.{}.test.index".format(dataset))
    test_idx_range = np.sort(test_idx_reorder)

    if dataset == 'citeseer':
        # Fix citeseer dataset (there are some isolated nodes in the graph)
        # Find isolated nodes, add them as zero-vecs into the right position
        test_idx_range_full = range(min(test_idx_reorder), max(test_idx_reorder)+1)
        tx_extended = sp.lil_matrix((len(test_idx_range_full), x.shape[1]))
        tx_extended[test_idx_range-min(test_idx_range), :] = tx
        tx = tx_extended

    features = sp.vstack((allx, tx)).tolil()
    features[test_idx_reorder, :] = features[test_idx_range, :]
    adj = nx.adjacency_matrix(nx.from_dict_of_lists(graph))
    return adj, features


if __name__ == '__main__':
    dataset = 'pubmed'
    adj, feature = load_data(dataset)
    # f_d = adj.todense()
    # a = np.array(f_d)
    # for i in range(len(a)):
    #     print(len(a[i]))
    # print('len_a', len(a))
    # set_printoptions(threshold='nan'
    # np.set_printoptions(threshold=np.nan)
    print(adj)
