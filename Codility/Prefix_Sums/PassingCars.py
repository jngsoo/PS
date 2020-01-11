# O(N) (PASS)
def solution(A):
    counter = 0
    answer = 0
    for car in A:

        if car == 0:
            counter += 1
        elif car == 1:
            answer += counter
    if answer > 1000000000:
        return -1

    return answer

print(solution([0,1,0,1,1]))

