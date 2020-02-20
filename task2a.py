import sys

def initiate(file):
    Ifile = open(file, 'r')
    totalErr = {}
    for line in Ifile:
        keys = line.split()
        totalErr[keys[0]] = int(keys[1])
    Ifile.close()
    return totalErr



def theMostFrequentError(file):
    totalErr = {}
    Ifile = open(file, 'r')
    

    for line in Ifile:
        lineErr = line.split()
        if len(lineErr) == 2:
            PErr = lineErr[1].split('|')
            for Err in PErr:
                counter = 0
                if Err in totalErr:
                    counter = totalErr[Err]
                totalErr[Err] = counter + 1

    mostFrequentErr = {"NameKey": '', "RepKey": 0}
    for Err, rep in totalErr.items():#actually finding the most frequent one
        if mostFrequentErr["RepKey"] <rep:
            mostFrequentErr["NameKey"] = Err
            mostFrequentErr["RepKey"] = rep
    Ifile.close()
    return mostFrequentErr



def calculateAll(file_students_path, most_freq_err, TotalErr):
    Sfile = open(file_students_path, 'r')

    gradesAfterFactor = {}
    GradesWithoutFactor = {}
    for line in Sfile:
        studentsKeys = line.split()
        gradesAfterFactor[studentsKeys[0]] = 100#initialization
        GradesWithoutFactor[studentsKeys[0]] = 100#initialization
        if len(studentsKeys) == 2:
            ErrForStudent = studentsKeys[1].split('|')
            for error in ErrForStudent:
                dec_points_by_error = error.split(':')
                points_to_dec = TotalErr[dec_points_by_error[0]]
                percentage = dec_points_by_error[1]
                total_dec = points_to_dec * float(percentage)
                GradesWithoutFactor[studentsKeys[0]] = GradesWithoutFactor[studentsKeys[0]] - float(total_dec)
                if error != most_freq_err["NameKey"]:
                    gradesAfterFactor[studentsKeys[0]] = gradesAfterFactor[studentsKeys[0]] - float(total_dec)

    gradesSum = 0
    factoredGradesSum = 0
    totalStudents = 0
    for student, grade in GradesWithoutFactor.items():
        print(str(student) + ": " + str(grade) + " => " + str(gradesAfterFactor[student]))
        gradesSum = gradesSum + grade
        factoredGradesSum = factoredGradesSum + gradesAfterFactor[student]
        totalStudents += 1

    avgBefore = (str(gradesSum / totalStudents))[:4]
    avgAfter = (str(factoredGradesSum / totalStudents))[:4]

    print("The average before factor is: " + avgBefore + " => The average after the factor is: " + avgAfter)


if __name__ == '__main__':
    file_students_grades = "lab10_grades.txt"
    file_err_codes = "error-codes"

    most_freq_err = theMostFrequentError(file_students_grades)
    TotalErr = initiate(file_err_codes)
    calculateAll(file_students_grades, most_freq_err, TotalErr)
