import sys


totalErr = {}
Ifile = open(sys.argv[1],'r')
for line in Ifile:
    ErrInLine = line.split('|')
    totalErr[ErrInLine[0]] = ErrInLine[1]
    
    
    
sor = sorted(totalErr.iteritems(), key=lambda (k,v): (v[1]), reverse=True)
   

print("The most frequent error in the file is " + (sor[0][0]) + " and was found " +
      (str)(sor[0][1]) + " times.")

Ifile.close()
