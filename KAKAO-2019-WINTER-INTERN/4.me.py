k = 10
room_number = [1,3,4,1,3,1]
# res should be [1,3,4,2,5,6]

def hashFunc1(n,modular):
    return n%modular

def hashFunc2(n, modular):
    return 1+n%modular

def doubleHashing(n, i, modular):
    return (hashFunc1(n, modular) + i*hashFunc2(n, modular)) % modular

def solution(k, room_number):
    answer = []
    for req in room_number:
        if req not in answer:
            answer.append(req)
        else:
            i = 0
            while req in answer:
                req += doubleHashing(req, i, k)
                i += 1
                if req > k:
                    req %= 10
            answer.append(req)

    return answer

print(solution(k, room_number))