import numpy as np
import scipy.spatial.distance as dist  # 导入scipy距离公式


Nets = {'drugDisease', 'drugsideEffect', 'proteinDisease'};
rootPath = '/Users/shw/code/DT_GCN'

for i in Nets:
	print(i)
	inputID = rootPath + '/data/' + i + '.txt'
	M = np.loadtxt(inputID)
	sim = 1 - dist.pdist(M, 'jaccard')
	sim = dist.squareform(sim)
	sim = sim + np.eye(M.shape[0])
	print(sim.shape)
	outputID = rootPath + '/simNet/Sim_' + i + '.txt'
	np.savetxt(outputID, sim, delimiter='\t')







