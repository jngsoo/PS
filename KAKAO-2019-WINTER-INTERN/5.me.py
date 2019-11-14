

def solution(stones, k):
    answer = 0
    no_stone = 0
    flag = True
    people = 0
    while flag:
        for i in range(len(stones)):
            if no_stone >= k:
                flag = False
                return people
            if stones[i] > 0:
                stones[i] -= 1
                no_stone = 0
            else:
                no_stone += 1
        if flag:
            people += 1

    answer = people
    return answer


def solution2(stones, k):
    answer = 0
    no_stone = 0
    flag = True
    people = 0
    while flag:
        for i in range(len(stones)):
            if no_stone >= k:
                flag = False
                return people

            if stones[i] > 0:
                stones[i] -= 1
                no_stone = 0
            else:
                no_stone += 1
        if flag:
            people += 1

    answer = people
    return answer

ts = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
tk = 3
# result == 3

ts1 = [1]
print(solution2(ts, tk))