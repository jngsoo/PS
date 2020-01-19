# EASY O(N) PASS
def solution(S):
    stack = []
    for c in S:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return 0
            stack.pop()
    if stack:
        return 0

    return 1

