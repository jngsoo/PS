# 시간 초과

def solve():
    n = int(input())
    resultArray = []
    countingDict ={}
    for _ in range(n):
        inserted = False
        inputNum = int(input())

        # Handle first input
        if not len(resultArray):
            resultArray.append(inputNum)
            countingDict[inputNum] = 1
            continue

        # Insert to array (with sorting)
        for i in range(len(resultArray)):
            if resultArray[i] > inputNum:
                resultArray.insert(i, inputNum)
                inserted = True
                break
        if not inserted:
            resultArray.append(inputNum)

        # Insert to Dict
        if inputNum not in countingDict:
            countingDict[inputNum] = 1
        elif inputNum in countingDict:
            countingDict[inputNum] += 1

    # Sorting Dict
    countingDict = {k: v for k, v in sorted(countingDict.items(), key=lambda item: item[1], reverse=True)}

    # Caculating

    avrg = round(sum(resultArray)/len(resultArray))
    median = resultArray[(len(resultArray)-1)//2]
    mode = list(countingDict.items())[0][0]
    diff = max(resultArray) - min(resultArray)

    print(avrg)
    print(median)
    print(mode)
    print(diff)

solve()