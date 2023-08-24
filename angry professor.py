def angryProfessor(k, a):
    students_on_time = 0
    for time in a:
        if time < 1:
            students_on_time += 1
    if students_on_time >= k:
        return "NO"
    else:
        return "YES"
