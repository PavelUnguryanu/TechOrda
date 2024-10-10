def find_min(arr):
    if not arr:
        return 0
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum
array = [1, 2, 3]
print(find_min(array))