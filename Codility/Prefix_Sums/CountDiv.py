import math
# O(1) PASS
'''
예를들어 0부터 11까지 2로 나누어 떨어지는 수는 floor(11 / 2) = 5개 이다.
그럼 A부터 B까지 K로 나누어 떨어지는 수는 floor(B / K) - floor((A - 1) / K) 이다. 
A - 1로 한 것은 A또한 나누어 떨어지는 수에 포함되어 있기 때문이다.
'''
def solution(A, B, K):
    answer = math.floor(B / K) - math.floor((A - 1) / K)
    return answer


# O(B-A) (50% pass, time out)
def solution_trash(A, B, K):
    answer = 0
    for num in range(A, B + 1):
        if num % K == 0:
            answer += 1

    return answer