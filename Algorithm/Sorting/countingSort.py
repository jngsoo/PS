def countingSort(A, k):
    n = len(A)
    count = [0] * (k + 1)
    for i in range(n):
        count[A[i]] += 1
    p = 0
    print(count)
    for i in range(k + 1):
        if count[i]:
            A[p] = i
            p += 1
    return A

print(countingSort([2,5,3,77,1],77))