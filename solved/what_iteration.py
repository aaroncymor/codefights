def whatIteration(arr):
    i = 0
    swapped = False
    iterations = 0
    while i < len(arr):
        if (i + 1) < len(arr):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                swapped = True
        print i, arr
        if (i + 1) == (len(arr) - 1) and swapped == True:
            i, swapped = 0, False
            iterations += 1
        elif (i + 1) ==(len(arr) - 1) and swapped == False:
            break
        else: i += 1
    return arr, iterations

print whatIteration([3,1,5,6,2,4,7,8])