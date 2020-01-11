'''
Caution
1) 배열에 원소가 하나일 경우
'''

# O(N) or O(N * log(N)) (PASS)
def solution(A):
    if not A:
        return 1

    A.sort()
    min = A[0]
    max = A[-1]

    if min != 1:
        return 1
    if max == len(A):
        return max + 1
    for i in range(1, len(A)):
        if A[i] - A[i - 1] > 1:
            return A[i] - 1


