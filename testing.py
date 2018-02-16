from file_loading import *
import numpy as np

subfamilies = load_subfamilies("Subfamilies.txt")

file = open("reads.fasta",'w')
i = 0
for fam in subfamilies.keys():
    for j in range(100):
        file.write('>read '+str(i)+'\n')
        file.write(subfamilies[fam][1]*int(np.random.rand()*20+10) +'\n')
        i+=1
file.close()
