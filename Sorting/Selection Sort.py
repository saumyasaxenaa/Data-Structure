numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(arr):
    i = 0
    while i < len(arr):
        min = i #setting the current index as minimum
        temp = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]: # update min if current value is lower than that
                min = j
        arr[i], arr[min] = arr[min], temp
        i += 1
    return arr

print(selectionSort(numbers))


