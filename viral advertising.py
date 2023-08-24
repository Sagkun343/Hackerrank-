def viralAdvertising(n):
    number_of_days = n
    people_shared_to = 5
    people_liked_total = 0
    for day in range(n):
        people_liked_per_day = people_shared_to // 2
        people_liked_total += people_liked_per_day
        people_shared_to = people_liked_per_day * 3
    return people_liked_total