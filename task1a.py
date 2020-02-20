import sys

Ifile=open(sys.argv[1],'r')
errorT={}

for line in Ifile:
    lineErr=line.split() #split the string into words
    if len(lineErr)==2:
        parsed= lineErr[1].split('|')
        for err in parsed:
            counter=0
            name=err.split(':')[0]
            if name in errorT:
                counter= errorT[name]
            errorT[name]=counter+1

Ofile= open("errorcodes.stats","w")


for key, errCount in errorT.items():
    Ofile.write(key+'|'+str(errCount)+'\n')

Ofile.close()

