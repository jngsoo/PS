
def solution(A):
    pass

# Logic error. 55% PASS
def solution_try(A):

    neg_count = 0
    N = len(A)
    left = 0
    right = N-1
    count = 0
    if N==3:
        return A[0]*A[1]*A[2]

    A.sort()

    if A[0] * A[1] < 0:
        return A[-1] * A[-2] * A[-3]

    answer = 1
    while count < 3:
        if abs(A[left]) <= abs(A[right]) or neg_count >= 2 or (neg_count == 0 and count == 2):
            answer *= A[right]
            right -= 1
            count += 1
        else:
            answer *= A[left]
            left += 1
            neg_count += 1
            count += 1
    return answer
t1 = [-3, 1, 2, -2, 5, 6]
res = solution(t1)
print(res)
