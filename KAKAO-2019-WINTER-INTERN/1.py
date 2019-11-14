def solution(board, moves):
    answer = 0
    answerList = []
    rotatedBoard = []
    for row in range(0, len(board)):
        tempList = []
        for col in range(len(board) - 1, -1, -1):
            tempList.append(board[col][row])
        rotatedBoard.append(tempList)

    for move in moves:
        for col in range(len(board) - 1, -1, -1):
            if not rotatedBoard[move - 1][col]:
                continue
            else:
                answerList.append(rotatedBoard[move - 1][col])
                if len(answerList) > 1:
                    if answerList[-1] == answerList[-2]:
                        for _ in range(2):
                            answerList.pop()
                        answer += 2
                rotatedBoard[move-1][col] = 0
                break

    return answer