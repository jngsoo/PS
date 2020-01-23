# PASS. using counter array structure
def solution(X, A):
    counter = [0 for _ in range(X)]
    tot = X*(X+1)//2
    for sec, leaf in enumerate(A):

        if leaf <= X and counter[leaf-1] == 0:
            counter[leaf-1] += 1
            tot -= leaf
        if tot == 0:
            return sec

    return -1

print(solution(5,[1,2,3,3,3,4,4,5,4,5]))
print(solution(1,[2]))


'''
27% Pass. Runtime err, timeout err
'''
def solution_fail(X, A):
    steps = []
    for sec, leaf in enumerate(A):
        if leaf not in steps:
            steps.append(leaf)
        if len(steps) == X:
            return sec


