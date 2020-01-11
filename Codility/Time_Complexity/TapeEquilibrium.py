# O(N) (PASS)
def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])

    left = A[0]
    right = sum(A[1:])
    min = abs(left - right)

    for pivotIdx in range(1, len(A) - 1):
        left += A[pivotIdx]
        right -= A[pivotIdx]
        tempAnswer = abs(left - right)

        if tempAnswer < min:
            min = tempAnswer

    return min


# O(N * N)
# 시간 초과 (53% 통과) sum을 계속 구했던게 비효율
def solution_trash(A):
    if len(A) == 2:
        return abs(A[0] - A[1])
    min = abs(sum(A[:1]) - sum(A[1:]))
    for i in range(2, len(A)):
        temp_difference = abs(sum(A[:i]) - sum(A[i:]))
        if temp_difference < min:
            min = temp_difference

    return min

