def compareTwoId(id, blurred_id):
    if len(id)!=len(blurred_id):
        return False

    for i in range(len(blurred_id)):
        if blurred_id[i]=="*":
            continue
        else:
            if blurred_id[i] != id[i]:
                return False

    return True     # 두 아이디 일치하면 True

def solution(user_id, banned_id):
    answer = 0
    for b_id in banned_id:
        for id in user_id:
            if compareTwoId(id, b_id):
                answer += 1
                user_id.remove(id)
            print(user_id)

    return answer

print(compareTwoId("frodo", "fr*d*",))