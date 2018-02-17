"""
This finds the most probably satellite subfamily for each
read in a fasta file
"""
from file_loading import *
from utils import *
from classify import *
import numpy as np

#load and process files
subfamilies = load_subfamilies("subfamilies.txt")
mers = load_mers("24mers.txt")
probs = get_probs(mers,subfamilies)
reads = load_reads("reads.fasta")
lookup = subfamilies.keys()

#classify each read
for read in reads:
    pred = classify(read.seq,probs)
    subfamily = lookup[np.argmax(pred)]
    print(read.description+" "+subfamily)
