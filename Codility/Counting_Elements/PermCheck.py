def solution(A):
    A.sort()
    for i in range(len(A)):
        if i+1 != A[i]:
            return 0

    return 1


# check if Array A is pertutation
# 83% PASS
def solution_trash(A):
    max = 0
    for num in A:
        if num >= max:
            max = num

    if max == len(A) and A.count(max) == 1:
        return 1
    return 0