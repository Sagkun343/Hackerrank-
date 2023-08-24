def breakingRecords(scores):
    min = max = scores[0]
    min_count = max_count = 0
    for i in range(1, len(scores)):
        if scores[i]>max:
            max = scores[i]
            max_count += 1
        elif scores[i]<min:
            min = scores[i]
            min_count += 1
    return [max_count, min_count]