# PASS
def solution(N, A):
    counter = [0] * N
    max_counter = next_max_counter = 0
    for elem in A:
        if elem <= N:
            current_counter = counter[elem - 1] = max(counter[elem - 1] + 1, max_counter + 1)
            next_max_counter = max(current_counter, next_max_counter)
        else:
            max_counter = next_max_counter

    return [v if v > max_counter else max_counter for v in counter]

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

