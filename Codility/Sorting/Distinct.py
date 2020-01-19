# PASS
def solution(A):
    A.sort()

    N = len(A)
    if N < 2:
        return N

    distinct = 1
    for i in range(1, N):
        if A[i] != A[i - 1]:
            distinct += 1

    return distinct