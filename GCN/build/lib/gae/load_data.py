import pickle as pkl


with open("DDT.emb.pkl", 'rb+') as f:
    x = pkl.load(f, encoding='latin1')
    print(x)
    print(x.shape)


