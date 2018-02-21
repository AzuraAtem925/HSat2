import numpy as np

"""
This generates the probability that a given read is in each subfamily
"""
def classify(read,probs):
    prob = np.ones(14)
    for i in range(len(read)-24):
        mer = read[i:i+24]
        if(probs.has_key(mer)):
            prob = np.multiply(prob,probs[mer])
    pred = np.divide(prob,np.sum(prob))
    return pred
