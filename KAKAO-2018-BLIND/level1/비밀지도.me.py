# 맞춤. 쉬운편. 십진수 => 이진수 변환
# 의도는 비트연산이니까 비트연산으로 풀어보자

'''
매개변수	값
n	    5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	    ["#####","# # #", "### #", "# ##", "#####"]

매개변수	값
n	    6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	    ["######", "### #", "## ##", " #### ", " #####", "### # "]
'''
def dec2BinStr(strLen, decimal):
    binEx = bin(decimal)
    res = binEx[2:]
    if len(res) < strLen:
        res = '0' * (strLen - len(res)) + res
    return res

def solution(n, arr1, arr2):
    answer = []
    for line in range(n):
        lineString = ''
        map1BinStr = dec2BinStr(n, arr1[line])
        map2BinStr = dec2BinStr(n, arr2[line])
        print(map1BinStr)
        for i in range(n):
            if (map1BinStr[i]=='1' or map2BinStr[i]=='1'):
                lineString += "#"
            else:
                lineString += ' '

        answer.append(lineString)

    return answer

print(solution(6, [45, 33, 33, 22, 31, 50], [27 ,56, 19, 14, 14, 10]))