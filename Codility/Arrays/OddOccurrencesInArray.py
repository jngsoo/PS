
# using hash (PASS)
# O(N) or O(N*log(N))
def solution(A):
    num_dict = {}
    answer_stack = []
    for num in A:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            del num_dict[num]

    return list(num_dict.keys())[0]

# 일부 시간 초과 (66% 통과)
# N^2
def solution_incomplete(A):
    tested = []
    for elem in A:
        if elem in tested:
            continue
        if A.count(elem) % 2 == 1:
            return elem
        tested.append(elem)


# 시간 초과
def solution_trash(A):
    for elem in A:
        if A.count(elem) % 2 == 1:
            return elem
