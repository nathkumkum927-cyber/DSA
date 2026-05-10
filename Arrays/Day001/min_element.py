def min_val(arr):
    min_val = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return arr
print(min_val([11,3,2,5,31,8]))
