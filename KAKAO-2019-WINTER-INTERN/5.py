def solution(stones, k):
    answer = 0
    idx = 0


    while True:
        for i in range(len(stones)):
            if stones[i] > 0:
                stones[i] -= 1

            elif stones[i] == 0:
                idx = i;
                while True:
                    if stones[idx] > 0:
                        if idx - (i - 1) < k:
                            break
                        else:
                            return answer
                    else:
                        idx += 1
                        if idx >= len(stones):
                            break;
        answer += 1
    return answer

st = [1,1,1,1,1]
sk =
print(solution(st, sk))