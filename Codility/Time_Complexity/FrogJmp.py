import math

def solution(X, Y, D):
    distance = Y - X
    if distance == 0:
        return 0

    return math.ceil(distance / D)
