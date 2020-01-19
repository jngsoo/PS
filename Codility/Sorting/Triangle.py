# O(N*log(N)) (PASS)
def solution(A):
    if len(A) < 3:
        return 0

    A.sort()
    N = len(A)

    memo_sum = A[0] + A[1]
    for i in range(2, N):
        if A[i] < memo_sum:
            return 1
        memo_sum = memo_sum - A[i - 2] + A[i]

    return 0



