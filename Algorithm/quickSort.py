def devide_and_conquer(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for idx in range(low, high):
        if arr[idx] < pivot:
            i += 1
            arr[i], arr[idx] = arr[idx], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):

    if low < high:
        idx = devide_and_conquer(arr, low, high)
        quick_sort(arr, low, idx - 1)
        quick_sort(arr, idx + 1, high)


test_case = [10,5,3,8,6,9,1]
quick_sort(test_case, 0, len(test_case)-1)
print(test_case)