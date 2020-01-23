def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [0,0,0]

    N = len(answers)
    for i in range(N):
        if answers[i] == a[i%len(a)]:
            answer[0] += 1
        if answers[i] == b[i%len(b)]:
            answer[1] += 1
        if answers[i] == c[i%len(c)]:
            answer[2] += 1

    winner_score = max(answer)
    winner = []
    for i, p in enumerate(answer):
        if p == winner_score:
            winner.append(i + 1)


    return winner

print(solution([1,3,2,4,2]))