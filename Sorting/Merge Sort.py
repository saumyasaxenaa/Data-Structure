numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    mid = length//2
    left = arr[:mid]
    right = arr[mid:]
    # print(f'Left: {left}')
    # print(f'Right: {right}')

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    leftindex = 0
    rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1
    return result + left[leftindex:] + right[rightindex:]


print(mergeSort(numbers))