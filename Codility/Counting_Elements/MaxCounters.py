def solution(N, A):
    pass

print(solution(5, [3,4,4,6,1,4,4]))


# Time out (66% pass)
# O(N*M)
def solution_trash(N, A):
    counter = {}
    for i in range(1,N + 1):
        counter[i] = 0
    max = 0
    carry = 0
    for num in A:
        if num == N + 1:
            for key in counter:
                counter[key] = max
        elif num in counter:
            counter[num] += 1
            if counter[num] > max:
                max = counter[num]

    return list(counter.values())

