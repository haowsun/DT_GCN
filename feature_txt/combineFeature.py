import numpy as np
import pickle as pkl

ALL_NAME = {1: "rep_drug_disease",
            2: "rep_drug_drug",
            3: "rep_drug_se",
            4: "rep_p_p",
            5: "rep_protein_disease",
            6: "rep_sim1_drug",
            7: "rep_sim2_drug",
            8: "rep_sim3_drug",
            9: "rep_sim4_drug",
            10: "rep_sim5_drug",
            11: "rep_sim6_drug",
            12: "rep_sim1_protein",
            13: "rep_sim2_protein",
            14: "rep_sim3_protein",
            15: "rep_sim4_protein"}
drugList = ["rep_drug_disease", "rep_drug_drug", "rep_drug_se", "rep_sim1_drug", "rep_sim2_drug",
            "rep_sim3_drug", "rep_sim4_drug", "rep_sim5_drug", "rep_sim6_drug"]

proteinList = ["rep_p_p", "rep_protein_disease", "rep_sim1_protein",
               "rep_sim2_protein", "rep_sim3_protein", "rep_sim4_protein"]

for i in range(len(drugList)):
    m = np.loadtxt(drugList[i] + ".txt")
    if i == 0:
        drugFeature = m
    else:
        drugFeature = np.concatenate([drugFeature, m], axis=1)


for i in range(len(proteinList)):
    m = np.loadtxt(proteinList[i] + ".txt")
    if i == 0:
        proteinFeature = m
    else:
        proteinFeature = np.concatenate([proteinFeature, m], axis=1)

print(drugFeature)
print(drugFeature.shape)

print(proteinFeature)
print(proteinFeature.shape)

Feature = np.concatenate([drugFeature, proteinFeature], axis=0)
print(Feature.shape)
print(type(Feature))

with open('DT.feature.pkl', 'wb') as f:
    pkl.dump(Feature, f)
