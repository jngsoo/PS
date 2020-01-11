# O(N) or O(N * log(N)) (PASS)
def solution(A):
    num_dict = {}
    for num in A:
        if num < 1:
            continue
        if num not in num_dict:
            num_dict[num] = True

    num_list = sorted(list(num_dict.keys()))

    if not num_list:
        return 1

    for i in range(len(num_list)):
        if (i + 1) != num_list[i]:
            return i + 1

    return len(num_list) + 1

print(solution([1,2,3]))
