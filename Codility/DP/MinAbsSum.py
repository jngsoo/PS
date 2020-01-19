def solution(A):
    N = len(A)
    if N==0:
        return 0
    dp = [A[0]] + ([0]*(N-1))

    for i in range(1,N):
        dp[i] = min(abs(dp[i-1] - A[i]), abs(dp[i-1] + A[i]))
    print(dp)
    return dp[-1]

t1 = [2,4,5,-1,6,-4,-7]
print(solution(t1))