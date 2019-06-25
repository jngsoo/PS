nofbd = int(input())
bds = input().split()
dist = []


best = 1
for i in range(nofbd):
    for j in range(i+1,len(bds)):
        if bds[i] >= bds[j]:
            best += 1
        else:
            break
    dist.append(best)
    best = 1

print(max(dist))
