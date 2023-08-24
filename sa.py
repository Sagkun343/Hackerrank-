def gradingStudents(grades):
    arr = []
    for i in range(len(grades)):
        if grades[i]<38 or grades[i]%5<3:
            arr.append(grades[i])
        elif grades[i] %5 > 2:
            arr.append(grades[i]-(grades[i]%5)+5)
    return arr

gradingStudents([20,40,32, 63, 43, 91])