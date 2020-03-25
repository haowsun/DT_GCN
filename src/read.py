import numpy as np
list = {0:'drugdrug.txt',1:'proteinprotein.txt',2:'drugsideEffect.txt'}

num = 2


M = np.loadtxt('../data/' + list[num])
print(list[num])
print(M.shape)
