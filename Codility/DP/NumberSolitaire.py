# O(N) PASS
def solution(A):
    N = len(A)
    dp = [0] * N
    dp[0] = A[0]

    for i in range(1, N):
        dp[i] = max(dp[max(0,i-6):i]) + A[i]

    return dp[-1]

t1 = [1,-2,0,9,-1,-2]
print(solution(t1))
