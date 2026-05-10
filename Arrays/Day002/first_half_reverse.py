def reverse_half(arr):
    start = 0
    end = len(arr)//2 -1
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr  
print(reverse_half([3,50,6,21,10,4]))                                                                                                                                                                                                                                                           


