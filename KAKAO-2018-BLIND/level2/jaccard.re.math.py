# 깔끔하지만 시간복잡도 조금 높게 나옴

import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    intersect = set(str1) & set(str2)
    union = set(str1) | set(str2)
    print(intersect)
    print(union)

    if len(union) == 0:
        return 65536

    inter_sum = sum([min(str1.count(twoLetter), str2.count(twoLetter)) for twoLetter in intersect])
    union_sum = sum([max(str1.count(twoLetter), str2.count(twoLetter)) for twoLetter in union])

    return math.floor((inter_sum/union_sum)*65536)
