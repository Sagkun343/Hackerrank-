def interferometries(number_of_collectibles):
    average_tries = 0
    iterator = 1
    while iterator <= number_of_collectibles:
        average_tries += (number_of_collectibles / iterator)
        iterator += 1
    return [average_tries, (number_of_collectibles / average_tries) * 100]


print(interferometries(3))
