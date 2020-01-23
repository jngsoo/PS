def solution2(citations):
    for h_index in range(max(citations), -1, -1):
        accum = 0
        for citation in citations:
            if citation >= h_index:
                accum += 1
            if accum == h_index:
                return h_index

def solution(citations):
    for i, citation in enumerate(sorted(citations)):
        print(i, citation)
        if citation >= len(citations) - i:
            return len(citations) - i
    return 0





# t1 = [10, 50 , 100]
# t1 = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5]
t1 = [0 ,1, 3, 3, 5, 6]
print(solution(t1)) # 3