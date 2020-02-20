import sys
import matplotlib.pyplot as mat


errFile= open(sys.argv[1], 'r')
codeFile= open(sys.argv[2],'r')

errCodeArr={}

for line in codeFile:
    keys=line.split()
    errCodeArr[keys[0]]=int(keys[1])

grades={}
for line in errFile:
    keys=line.split()
    grades[keys[0]]=100
    if len(keys)==2:
        singleS=keys[1].split('|')
        for err in singleS:
            decrease = err.split(':')
            howMuch=errCodeArr[decrease[0]]
            percentage= decrease[1]
            total=howMuch*float(percentage)

            grades[keys[0]]=grades[keys[0]]-float(total)

Ofile=open("final_grades", 'r+')
for student, hisFinalGrade in grades.items():
    Ofile.write(str(student)+'|'+str(hisFinalGrade)+'\n')


arr=[]

for line in Ofile:
    splited= line.split("|")
    arr.append(splited[1])

num_bins = 5
n, bins, patches = mat.hist(arr, num_bins, facecolor='orange', alpha=0.5)
mat.show()


Ofile.close()
