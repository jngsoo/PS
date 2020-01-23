# def count(A):
#     counter = [0] * (max(A)+1)
#     for num in A:
#         counter[num] += 1
#
#     return counter

def countingSort(A, k):
    n = len(A)
    count = [0] * (k + 1)
    for i in range(n):
        count[A[i]] += 1
    p = 0
    print(count)
    for i in range(k + 1):
        for j in range(count[i]):
            A[p] = i
            p += 1
    return A

# print(countingSort([2,5,3,77,1,1,1],77))

def fibo_bottom_up(n):
    bottom_up = [None] * n
    bottom_up[0] = 1
    bottom_up[1] = 1
    for i in range(2, n):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]

    return bottom_up[n-1]

# print(fibo_bottom_up(10000))

def dp_simple(A):
    N = len(A)
    dp = [A[0]] + [0]*(N-1)
    for i in range(1,N):
        dp[i] = max(dp[max(0,i-6):i]) + A[i]
    print(dp)
    return dp[-1]


# ans = dp_simple([1,-2,0,9,-1,-2, -3, 5, 1])
# print(ans)

def dp_coin(C,k):
    MAX_INT = 100000000
    n = len(C)
    dp = [0] + [MAX_INT] * k
    for i in range(1, n + 1):
        for j in range(C[i - 1], k + 1):
            dp[j] = min(dp[j - C[i - 1]] + 1, dp[j])
            print(f'i = {i}, j = {j}, C[i-1] = {C[i-1]} dp = {dp}')
    return dp

# print(dp_coin([1,3,4],6))

def swap_string(string):
    string = list(string)
    n = len(string)
    start = 0
    end = n - 1
    while start < n/2:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1

    return ''.join(string)

# print(swap_string('hello world'))