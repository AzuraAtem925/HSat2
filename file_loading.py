'''Imports altemose data as dictionary. Key= sequence. Value= probability is
in a read.'''
import numpy as np

def load_probs(filepath):
    file= open(filepath,"r")
    pdic={}
    lis = file.readlines()
    del lis[0]
    for n in range(len(lis)):
        sdic = {}
        lis[n] = lis[n].rstrip()
        lis[n] = lis[n].split()
        mer = lis[n][0]
        fam = lis[n][1]
        prob = lis[n][2]
        sdic[fam] = prob
        pdic[mer] = sdic
    file.close
    return pdic

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
