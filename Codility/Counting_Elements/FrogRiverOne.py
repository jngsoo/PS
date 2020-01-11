def solution(X, A):
    pass


'''
로직 자체 에러
'''
def solution_trash(X, A):
    # write your code in Python 3.6
    leaves_list = []
    leaves_dict = {}

    for sec_idx in range(len(A)):

        if A[sec_idx] in leaves_dict:
            continue

        if A[sec_idx] not in leaves_dict:
            leaves_dict[sec_idx] = True
            leaves_list.append(A[sec_idx])

            if len(leaves_list) == X:
                return sec_idx

x = solution_trash(5,[1,2,3,3,3,4,4,5,4])
print(x)