def birthdayCakeCandles(candles):
    # Write your code here
    count = 0
    max_value = 0
    for i in range(len(candles)):
        if candles[i]>max_value:
            max_value = candles[i]
            count = 1
        elif candles[i] == max_value:
            count += 1
    return count