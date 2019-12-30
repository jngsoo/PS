def hanoi(n, start, end, via):
    if n==0:
        return
    hanoi(n-1, start, via, end)
    print(start, end)
    hanoi(n-1, via, end, start)

def recursive(n):
    if n==0:
        return
    recursive(n-1)
    print(n)
    # recursive(n-1)

recursive(5)

# hanoi(3,1,3,2)
