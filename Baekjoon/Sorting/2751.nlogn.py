# Get input
n = int(input())
userInputList = []
for _ in range(n):
    userInputNum = int(input())
    userInputList.append(userInputNum)

def mergeSort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    i = j = k = 0

    while (i < len(left)) and (j < len(right)):

        if (left[i] < right[j]):
            arr[k] = left[i]
            i += 1

        elif (left[i] >= right[j]):
            arr[k] = right[j]
            j += 1
        k += 1

    while (i < len(left)):
        arr[k] = left[i]
        i += 1
        k += 1

    while (j < len(right)):
        arr[k] = right[j]
        j += 1
        k += 1

# print(userInputList)
mergeSort(userInputList)
for elem in userInputList:
    print(elem)
