
def solution(s):
    s = s[1: len(s)-1]
    bracketStack = []
    s_idx = 0
    tempList = [None for _ in range(501)]
    tempSet = set()
    answerLen = 0
    tempDigitStr = ''

    for char in s:

        if char=='{':
            bracketStack.append(char)

        if char.isdigit():
            tempDigitStr += char

        # if char == ',' or s_idx==len(s)-1:
        if char==',':
            if len(bracketStack) == 0:
                tempList[len(tempSet)] = tempSet
                tempDigitStr = ''
                tempSet = set()
            else:
                tempSet.add(int(tempDigitStr))
                tempDigitStr = ''

        if char == '}':
            if tempDigitStr:
                tempSet.add(int(tempDigitStr))
                if len(tempSet) > answerLen:  # 답 길이 구하는 ex) [2,1,3,4] => answerLen = 4
                    answerLen = len(tempSet)
                tempList[len(tempSet)] = tempSet

        s_idx += 1
    answer = [list(tempList[1]).pop()]
    for i in range(1, answerLen):
        answer.append(list(tempList[i+1]-tempList[i]).pop())

    return answer


t0 = "{{}}"
t1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
t2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
t3 = "{{20,111},{111}}"
t4 = "{{123}}"
t5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

print(solution(t0))
print(solution(t1))
# print(solution(t2))
# print(solution(t3))
# print(solution(t4))
# print(solution(t5))

# 5번 이슈

