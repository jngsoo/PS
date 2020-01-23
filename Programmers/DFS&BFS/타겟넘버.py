answer = 0

def DFS(numbers, level, target, sum=0):
    if sum == target and level >= len(numbers):
        global answer
        answer += 1
        return

    elif level < len(numbers):
        DFS(numbers, level + 1, target, sum + numbers[level])
        DFS(numbers, level + 1, target, sum - numbers[level])
        return


def solution(numbers, target):
    global answer
    DFS(numbers, 0, target)
    return answer


# Driver code (should be 5)
print(solution([1, 1, 1, 1, 1], 3))
