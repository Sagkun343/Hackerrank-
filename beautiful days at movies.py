def beautifulDays(i, j, k):
    beautiful_day_counter = 0
    for number in range(i, j+1):
        number_str = str(number)
        number_str = number_str[::-1]
        reversed_number = int(number_str)
        print(abs(number - reversed_number))
        if abs(number - reversed_number) % k == 0:
            beautiful_day_counter += 1
    return beautiful_day_counter

beautifulDays(20, 23, 6)