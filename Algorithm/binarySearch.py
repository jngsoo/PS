def binarySearch(arr, left, right, target):
    if right < left:
        return -1
    print('bin-search!')
    mid = (left + (right + 1)) // 2
    print(left, mid, right)
    if arr[mid] == target:
        res = arr[mid]
        return res

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

    return binarySearch(arr, left, right, target)


t1 = [2,4,5,9,11,14,19]

print(binarySearch(t1, 0, len(t1)-1, 19))