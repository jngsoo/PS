'''
Caution
1) 배열의 길이 이상으로 rotate 시키는 경우
2) 빈 배열이 주어진 경우
3) 0번 rotate 하는 경
'''

def solution(A, K):
    if K == 0 or not A:
        return A
    arrayLength = len(A)
    if K > arrayLength:
        K %= arrayLength
    return A[arrayLength-K:] + A[:arrayLength-K]

print(solution([3, 8, 9, 7, 6],3))
print(solution([0,0,0],1))
print(solution([1, 1, 2, 3, 5], 42))