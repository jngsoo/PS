# O(N) PASS
def solution(S):
    stack = []

    for c in S:
        if c=='(' or c=='[' or c=='{':
            stack.append(c)

        elif c==')' or c==']' or c=='}':
            if not stack:
                return 0
            if c==')' and stack.pop() != '(':
                return 0
            if c==']' and stack.pop() != '[':
                return 0
            if c=='}' and stack.pop() != '{':
                return 0

    if stack:
        return 0
    return 1

print(solution(t1))