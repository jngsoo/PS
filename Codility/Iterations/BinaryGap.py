# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    binary = bin(N)[2:]
    temp_count = 0
    count_max = 0
    for c in binary:
        if c=='1' and count_max < temp_count:
            count_max = temp_count
            temp_count = 0

        if c=='0':
            temp_count += 1
    return count_max


print(solution(32))

