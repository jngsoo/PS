def solution(k, room_number):
    answer = []
    for req in room_number:
        if req not in answer:
            answer.append(req)
        else:
            while req in answer:
                req += 1
                if req > k:
                    req %= 10
            answer.append(req)

    return answer