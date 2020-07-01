numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(arr):
    l = 0
    while l < len(arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        l += 1
    return arr

print(bubbleSort(numbers))