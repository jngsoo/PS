

def DFS(computers, visited):
    for computer in computers:
        for adjacent_computer in computer:
            if not visited[adjacent_computer][computer] and not visited[computer][adjacent_computer]:
                visited[adjacent_computer][computer] = adjacent_computer
                visited[computer][adjacent_computer] = adjacent_computer


def solution(n, computers):
    answer = 0
    visited = [[False] * n] * n

    return answer

# Driver code (should be 2,1)
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

