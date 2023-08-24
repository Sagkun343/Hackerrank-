def rashid_game(total, array):
    position = 0
    length_of_array = len(array)
    if length_of_array == 0:
        return total
    if length_of_array == 1:
        return total + array[0]
    zeroth_position_profit = array[0] - array[1]
    last_position_profit = array[length_of_array-1] - array[length_of_array-2]
    addition = 0
    if last_position_profit > zeroth_position_profit:
        opportunity_cost = last_position_profit
        position = length_of_array - 1
        addition = array[length_of_array-1]
    else:
        opportunity_cost = zeroth_position_profit
        addition = array[0]
    for i in range(1, length_of_array-1):
        if (array[i] - array[i+1] - array[i-1]) > opportunity_cost:
            opportunity_cost = (array[i] - array[i+1] - array[i-1])
            position = i
            addition = array[i]
    if position == 0:
        return rashid_game(total + addition, array[2:])
    elif position == length_of_array-1:
        return rashid_game(total + addition, array[:length_of_array - 2])
    else:
        return rashid_game(total + addition, array[:position - 1] + array[position + 2:])


array = list(map(int, input().split()))
print(rashid_game(0, array))
