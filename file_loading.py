"""
These functions are for file loading
"""
import numpy as np
from Bio import SeqIO

"""
Load in the 24mer.txt file
"""
def load_mers(filepath):
    file= open(filepath,"r")
    mers={}
    lis = file.readlines()
    del lis[0]
    for n in range(len(lis)):
        lis[n] = lis[n].rstrip()
        lis[n] = lis[n].split()
        mer = lis[n][0]
        fam = lis[n][1]
        prob = float(lis[n][2])
        mers[mer] = [fam,prob]
    file.close
    return mers
"""
Loads in the file with subfamilies and background prob
"""
def load_subfamilies(filepath):
    file= open(filepath,"r")
    subfamilies={}
    fams = []
    nums = []
    consensus = []
    lis = file.readlines()
    for n in range(len(lis)):
        sdic = {}
        lis[n] = lis[n].rstrip()
        lis[n] = lis[n].split()
        fams += [lis[n][0]]
        nums += [float(lis[n][1])]
        consensus += [lis[n][2]]
    total = np.sum(nums)
    for n in range(len(fams)):
        subfamilies[fams[n]] = [nums[n]/total,consensus[n]]
    file.close
    return subfamilies
"""
Loads the fasta file into a biopython seqrecored object
"""
def load_reads(filepath):
    reads = SeqIO.parse(open(filepath),'fasta')
    return reads
