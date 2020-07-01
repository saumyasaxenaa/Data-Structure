numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(arr):
    length = len(arr)
    i = 1
    end = arr[0]
    while i < length:
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(i):
                if x < arr[j]:
                    arr.insert(j,x)
                    # print(arr)
                    break
        end = arr[i]
        i += 1
    return arr
print(insertionSort(numbers))


