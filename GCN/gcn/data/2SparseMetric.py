import numpy as np
import scipy.sparse as ss
import pickle as pkl
a = np.loadtxt('adj.txt', dtype=np.int32)
a = np.transpose(a)
# print(a)
a_1 = a[0]
a_2 = a[1]
# print(a_1, len(a_1))
# print('\n', a_2, len(a_2))
value = np.ones(len(a_1), dtype=np.int32)
# print('\n', value, len(value))

sparseM = ss.coo_matrix((value, (a_1, a_2)))
print(sparseM.shape)
# with open('adj.pkl', 'wb') as f:
#     pkl.dump(sparseM, f)

