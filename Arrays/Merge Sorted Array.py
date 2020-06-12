def mergeArray(arr1, arr2):

    if len(arr1) == 0:
        return arr2
    elif len(arr2) == 0:
        return arr1

    ind1, ind2 = 0, 0
    while ind1 < len(arr1) and ind2 < len(arr2):
        if(arr1[ind1] > arr2[ind2]):
            arr1.insert(ind1, arr2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1
    if ind2 < len(arr2)-1:
        arr1.extend(arr2[ind2:])
    return(arr1)

a = mergeArray([1,2,3,100],[5,7,9,10])
print(a)