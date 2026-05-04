def count_min_val(arr):
    min_val = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    count=0
    for i in range(len(arr)):
        if arr[i]==min_val:
            count+=1
    return count
print(count_min_val([1,10,3,23,1,6]))
