'''Imports altemose data as dictionary. Key= sequence. Value= probability is
in a read.'''

def main():
    data = open("gdata.txt","r")
    pdic={}
    lis = data.readlines()
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
   
main()
