# 풀었음. 맞춤. 길지만 제일 효율적(시간)

def strToObj(str):
    dic = {}
    for i in range(len(str)-1):
        if str[i].isalpha() and str[i+1].isalpha():
            twoLetterStr = str[i] + str[i+1]
            if twoLetterStr in dic:
                dic[twoLetterStr] += 1
            else:
                dic[twoLetterStr] = 1
    return dic

def intersectDic(dic1, dic2):
    resDic = {}
    for key in dic1:
        if key in dic2:
            resDic[key] = min(dic1[key], dic2[key])
    return resDic

def unionDic(dic1, dic2):
    resDic = {}
    # push dic2 to dic1
    for key in dic2:
        if key in dic1:
            if dic2[key] > dic1[key]:
                dic1[key] = dic2[key]
        else:
            dic1[key] = dic2[key]

    return dic1

def solution(str1, str2):
    answer = 1
    dic1, dic2 = strToObj(str1.lower()), strToObj(str2.lower())
    if(dic1 or dic2):
        answer = sum(list(intersectDic(dic1,dic2).values())) / sum(list(unionDic(dic1, dic2).values()))
    return int(answer * 65536)
