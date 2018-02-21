import numpy as np

"""
This function generates the baysian probability for each subfamily
given a sequence
""" 
def get_probs(mers,subfamilies):
    probs = {}
    lookup = subfamilies.keys()
    for mer in mers.keys():
        prob = np.ones(14)
        subfamily = mers[mer][0]
        p_subfamily = subfamilies[subfamily][0]
        a = mers[mer][1]*p_subfamily
        b = a+0.000001*(1-p_subfamily)
        for i in range(14):
            if lookup[i] == subfamily:
                prob[i] = a
            else:
                prob[i] = 0.000001*subfamilies[lookup[i]][0]/b
        probs[mer] = prob
    return probs
