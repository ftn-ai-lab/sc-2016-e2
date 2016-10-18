def q_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return q_sort(left) + middle + q_sort(right)
    
print q_sort([1, 3, 2, 34, 12, 15, 54, 11])   