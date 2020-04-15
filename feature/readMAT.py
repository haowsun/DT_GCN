import numpy as np
from scipy.io import loadmat
ALL_NAME = {1 : "rep_drug_disease", 
			2 : "rep_drug_drug",
			3 : "rep_drug_se",
			4 : "rep_p_p",
			5 : "rep_protein_disease",
			6 : "rep_sim1_drug",
			7 : "rep_sim2_drug",
			8 : "rep_sim3_drug",
			9 : "rep_sim4_drug",
			10 : "rep_sim5_drug",
			11 : "rep_sim6_drug",
			12 : "rep_sim1_protein",
			13 : "rep_sim2_protein",
			14 : "rep_sim3_protein",
			15 : "rep_sim4_protein"}

for i in ALL_NAME:
	print(ALL_NAME[i])

	m_name = ALL_NAME[i]
	m = loadmat(m_name + ".mat")
	m_array = m[m_name]
	print(m_array)
	print(m_array.shape)

	np.savetxt("../feature_txt/" + m_name + ".txt", m_array)