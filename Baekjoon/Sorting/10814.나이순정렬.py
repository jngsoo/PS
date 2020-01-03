def solve():
    resultDict = {}
    n = int(input())
    for _ in range(n):
        user = input().split()
        age = int(user[0])
        name = user[1]

        if age in resultDict:
            resultDict[age].append(name)
        if age not in resultDict:
            resultDict[age] = [name]

    sortedDict = sorted(resultDict.items())
    for tempDict in sortedDict:
        age = tempDict[0]
        for name in tempDict[1]:
            print(age, name)

solve()