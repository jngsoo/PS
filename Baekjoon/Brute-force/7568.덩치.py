def getInput():
    num = int(input())
    sizeList = []
    for _ in range(num):
        size = [int(i) for i in input().split()]
        sizeList.append(size)

    return sizeList

def solve():
    sizeList = getInput()
    rankList = []
    numOfPeople = len(sizeList)
    for i in range(numOfPeople):
        rank = 1
        for j in range(numOfPeople):
            if sizeList[i][0] < sizeList[j][0] and sizeList[i][1] < sizeList[j][1]:
                rank += 1
        rankList.append(rank)

    print(' '.join([str(i) for i in rankList]))

solve()