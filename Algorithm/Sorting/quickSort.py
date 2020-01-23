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

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))
# Prints "[1, 1, 2, 3, 6, 8, 10]"


