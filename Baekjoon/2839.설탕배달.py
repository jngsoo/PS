def find_min_bag(n):
    minBag = [-1 for _ in range(n + 1)]
    kg_list = [5, 3]

    if n >= 5:
        minBag[3] = 1
        minBag[5] = 1
    elif n >= 3:
        minBag[3] = 1

    for weight in range(6, n + 1):
        for kg in kg_list:
            for backward in range(1, weight):
                found = False
                if (minBag[weight - backward] is not -1) and (backward == kg):
                    minBag[weight] = minBag[weight - kg] + 1
                    found = True
                    break
            if found:
                break
    return minBag[n]

N = int(input())
print(find_min_bag(N))
