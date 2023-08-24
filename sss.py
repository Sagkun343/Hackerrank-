def find_majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        print(candidate)
        print("count: " +str(count))
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verification step
    count = sum(1 for num in arr if num == candidate)
    if count > len(arr) // 2:
        return candidate
    else:
        return None  # No majority element

# Example usage:
array = [1,2,1,2,1,2,1,2,1,2,1]
result = find_majority_element(array)
if result:
    print("Majority element:", result)
else:
    print("No majority element found.")
