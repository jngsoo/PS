'''
[3, 30, 34, 5, 9]	"9534330"
'''

t = [20, 200, 20]
t1 = [21, 212]
t2 = [0,0,1000,0]

def solution(int_list):
    if sum(int_list)==0:
        return '0'
    str_list = [str(elem) for elem in int_list]
    sorted_str_list = sorted(str_list,
                             key=lambda elem: (elem[0],
                                               elem[1] if len(elem)>1 else elem[len(elem)-1],
                                               elem[2] if len(elem)>2 else elem[len(elem)-1]),
                             reverse=True)
    answer = "".join(sorted_str_list)
    return answer

