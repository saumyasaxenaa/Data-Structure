def FirstRecurringChar(arr):
    if len(arr) == 1 or 0:
        return None
    count = {}
    for num in arr:
        if num in count:
            return num
        else:
            count[num] = 1
    return None
f = FirstRecurringChar([2,3,4,5,6,7,2])
print(f'The first recurring character is: {f}')