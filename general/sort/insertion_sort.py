def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1
            
    return arr

sorted = insertion_sort([5, 2, 4, 6, 1, 3])
print(sorted)

