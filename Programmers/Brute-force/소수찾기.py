def isPrime_mine(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True

# numbers [string]
def solution(numbers):
    answer = 0
    max_num = int(''.join(sorted(numbers, reverse=True)))
    for num in range(2, max_num + 1):
        if isPrime(num): answer += 1

    return answer

# print(solution('011'))
print(isPrime(241))